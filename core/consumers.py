import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.apps import apps

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope["user"].username  # Current user
        self.recipient = self.scope["url_route"]["kwargs"]["room_name"]

        # Ensure both users have the same room name
        self.room_group_name = f"chat_{'_'.join(sorted([self.sender, self.recipient]))}"

        print(f"WebSocket Connected: {self.room_group_name}")

        try:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        except Exception as e:
            print(f"WebSocket Connection Error: {e}")

    async def disconnect(self, close_code):
        print(f"WebSocket Disconnected: {self.room_group_name} (code: {close_code})")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        print(f"Raw Message Received: {text_data}")

        if not text_data.strip():
            print("Received Empty Message! Ignoring...")
            return

        try:
            data = json.loads(text_data)
            message = data.get("message")
            sender_username = data.get("sender")

            if not message or not sender_username:
                print("Invalid message format, missing keys")
                return

            print(f"Received: {sender_username}: {message}")

            # Determine the correct recipient
            recipient_username = self.get_actual_recipient(sender_username)

            # Send message to WebSocket group
            await self.channel_layer.group_send(
                self.room_group_name, 
                {"type": "chat_message", "message": message, "sender": sender_username}
            )

            # Send notification to the recipient
            if recipient_username and recipient_username != sender_username:
                await self.create_notification(recipient_username, sender_username, message)

        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Malformed Data Received: {text_data}")

    # Send chat messages to WebSocket
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        print(f"Sending Message: {sender}: {message}")

        await self.send(text_data=json.dumps({"message": message, "sender": sender}))

    # Extract recipient username
    def get_actual_recipient(self, sender_username):
        users = self.room_group_name.replace("chat_", "").split("_")
        recipient = users[0] if users[1] == sender_username else users[1]
        return recipient

    # Create notification for recipient when they receive a new chat message.
    @sync_to_async
    def create_notification(self, recipient_username, sender_username, message):
        Notification = apps.get_model('core', 'Notification')  

        try:
            User = apps.get_model('core', 'User')
            recipient = User.objects.get(username=recipient_username)
            sender = User.objects.get(username=sender_username)

            Notification.objects.create(
                user=recipient,
                message=f"{sender.username} sent you a chat message: '{message}'"
            )

            print(f"Notification Created: {recipient.username} received a message from {sender.username}")

        except User.DoesNotExist:
            print(f"User {recipient_username} does not exist. Notification not created.")