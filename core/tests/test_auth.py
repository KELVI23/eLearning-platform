from rest_framework.test import APITestCase
from rest_framework import status
from .factories import UserFactory

class AuthenticationTests(APITestCase):
    # Test user authentication (register, login, profile)

    def setUp(self):
        self.user = UserFactory(username="testuser", email="test@example.com")
        self.user.set_password("testpass")
        self.user.save()

    def test_register_user(self):
        # Ensure user can register
        data = {"username": "newuser", "password": "newpass", "email": "new@example.com", "role": "student"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        # Ensure user can login
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_invalid_login(self):
        # Ensure login fails with incorrect password
        data = {"username": "testuser", "password": "wrongpass"}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_profile(self):
        # Ensure user can access profile after login
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)