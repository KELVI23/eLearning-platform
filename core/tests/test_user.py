import factory
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "testpass")
    role = factory.Iterator(["student", "teacher"])

class UserTests(APITestCase):
    def setUp(self):
        # Create a teacher user for authentication
        self.teacher = UserFactory(role="teacher")
        self.client.force_authenticate(user=self.teacher)

