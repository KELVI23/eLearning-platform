from rest_framework.test import APITestCase
from rest_framework import status
from .factories import UserFactory, CourseFactory

class CourseTests(APITestCase):
    # Test course management (create, enroll, view)

    def setUp(self):
        self.teacher = UserFactory(role="teacher")
        self.student = UserFactory(role="student")
        self.client.force_authenticate(user=self.teacher)
        self.course = CourseFactory(teacher=self.teacher)

    # def test_create_course(self):
    #     # Ensure a teacher can create a course
    #     self.client.force_authenticate(user=self.teacher)  #  authenticate teacher
    #     data = {
    #         "title": "Advanced Django",
    #         "description": "Learn advanced Django",
    #         "students": [],
    #         "image_url": "https://example.com/course-image.jpg",
    #         "difficulty_level": "Intermediate",
    #     }
    #     response = self.client.post("/api/courses/create_course/", data)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data["teacher"], self.teacher.id) 


    def test_student_enrollment(self):
        # Ensure a student can enroll in a course
        self.client.force_authenticate(user=self.student)
        response = self.client.post(f"/api/courses/{self.course.id}/enroll/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course_list(self):
        # Ensure all users can retrieve course list
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)