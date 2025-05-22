from rest_framework.test import APITestCase
from rest_framework import status
from .factories import UserFactory, CourseFactory, FeedbackFactory

class FeedbackTests(APITestCase):
    """Test feedback system."""

    def setUp(self):
        self.student = UserFactory(role="student")
        self.course = CourseFactory()
        self.client.force_authenticate(user=self.student)

    def test_student_leave_feedback(self):
        """Ensure a student can leave feedback for a course."""
        data = {"course": self.course.id, "rating": 5, "comment": "Excellent course!"}
        response = self.client.post("/api/feedback/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_feedback(self):
        """Ensure users can view feedback for courses."""
        FeedbackFactory(course=self.course)
        response = self.client.get("/api/feedback/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)