"use client";
import { useState, useEffect } from "react";

interface User {
  id: number;
  username: string;
  role: string;
}

interface Message {
  sender: string;
  message: string;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [search, setSearch] = useState("");
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const [currentUser, setCurrentUser] = useState<string>("");

  useEffect(() => {
    // Fetch logged-in user
    const token = localStorage.getItem("access_token");
    if (!token) return;

    fetch("http://127.0.0.1:8000/api/profile/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setCurrentUser(data.username));

    // Fetch user contacts (students & teachers)
    fetch("http://127.0.0.1:8000/api/users/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);


// Connect to WebSocket when user is selected
useEffect(() => {
  if (!selectedUser) return;

  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const sanitizedUsername = selectedUser.username.replace(/ /g, "_");  // Replace spaces
  const chatRoom = `_`.concat(...[currentUser, sanitizedUsername].sort());
  const socketURL = `${protocol}://127.0.0.1:8001/ws/chat/${chatRoom}/`;

  const newSocket = new WebSocket(socketURL);
  
  newSocket.onopen = () => console.log("WebSocket Connected:", socketURL);

  newSocket.onmessage = (event) => {
      console.log("📩 WebSocket Message Received:", event.data);

      try {
          const receivedMessage = JSON.parse(event.data);

          setMessages((prev) => {
              if (!prev.some(msg => msg.sender === receivedMessage.sender && msg.message === receivedMessage.message)) {
                  return [...prev, receivedMessage];
              }
              return prev;
          });
      } catch (error) {
          console.error("Error parsing WebSocket message:", error);
      }
  };

  newSocket.onerror = (error) => console.error("WebSocket Error:", error);

  newSocket.onclose = (event) => {
      console.warn("WebSocket Closed:", event);
      if (event.code !== 1000) {
          console.log("Reconnecting in 5 seconds...");
          setTimeout(() => setSocket(new WebSocket(socketURL)), 5000);
      }
  };

  setSocket(newSocket);

  return () => {
      console.log("Closing WebSocket Connection");
      newSocket.close();
  };
}, [selectedUser]);

const sendMessage = () => {
  if (!socket || !selectedUser || !input.trim()) {
      console.warn("Cannot send empty message or WebSocket not available.");
      return;
  }

  if (socket.readyState !== WebSocket.OPEN) {
      console.warn("WebSocket is not open. Message not sent.");
      return;
  }

  const messageData = JSON.stringify({
      sender: currentUser,  
      message: input.trim(),
  });

  console.log("Sending WebSocket Message:", messageData);
  socket.send(messageData);

  // Add the message to state for sender
  setMessages((prev) => [...prev, { sender: currentUser, message: input.trim() }]);

  setInput("");  // Clear input field after sending
};

  return (
    <div className="p-10 min-h-screen bg-gray-100 dark:bg-gray-800 text-black flex flex-col">
      <h1 className="text-4xl font-bold mb-6 text-white">Chat</h1>

      {/* Search and Select User */}
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search users..."
          className="border p-2 rounded w-full"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <ul className="mt-2 max-h-40 overflow-y-auto bg-white dark:bg-gray-700 rounded shadow-md p-2">
          {users
            .filter((user) => user.username.toLowerCase().includes(search.toLowerCase()))
            .map((user) => (
              <li
                key={user.id}
                className={`p-2 cursor-pointer rounded hover:bg-blue-200 ${
                  selectedUser?.id === user.id ? "bg-blue-300" : ""
                }`}
                onClick={() => setSelectedUser(user)}
              >
                {user.username} ({user.role})
              </li>
            ))}
        </ul>
      </div>

      {/* Chat Window */}
      {selectedUser ? (
        <div className="flex flex-col h-96 bg-white dark:bg-gray-900 p-4 rounded shadow-md">
          <h2 className="text-2xl font-bold mb-4 text-white">Chat with {selectedUser.username}</h2>

          <div className="flex-1 overflow-y-auto flex flex-col gap-3">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`max-w-xs px-4 py-2 rounded-lg ${
                  msg.sender === currentUser
                    ? "bg-blue-500 text-white self-end"
                    : "bg-gray-300 text-black self-start"
                }`}
              >
                <p className="font-bold">{msg.sender}</p>
                <p>{msg.message}</p>
              </div>
            ))}
          </div>

          <div className="flex mt-4">
            <input
              className="border p-2 w-full rounded"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type a message..."
            />
            <button
              onClick={sendMessage}
              className="ml-2 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
              Send
            </button>
          </div>
        </div>
      ) : (
        <p className="text-gray-400 text-center mt-6">Select a user to start chatting</p>
      )}
    </div>
  );
}