from rest_framework.test import APITestCase
from rest_framework import status
from .factories import UserFactory, CourseFactory, SectionFactory, MaterialFactory
from django.core.files.uploadedfile import SimpleUploadedFile

class MaterialTests(APITestCase):
    # Test course material uploads and retrieval

    def setUp(self):
        self.teacher = UserFactory(role="teacher")
        self.student = UserFactory(role="student")
        self.client.force_authenticate(user=self.teacher)

        self.course = CourseFactory(teacher=self.teacher)
        self.section = SectionFactory(course=self.course)

    # Ensure teachers can upload materials
    def test_teacher_can_upload_material(self):
        self.client.force_authenticate(user=self.teacher)
        test_file = SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf")
        data = {
            "title": "Lecture Notes",
            "description": "Detailed lecture notes",
            "file": test_file,
            "section_id": self.section.id
        }
        response = self.client.post(f"/api/sections/{self.section.id}/materials/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_student_cannot_upload_material(self):
        # Ensure students cannot upload materials
        self.client.force_authenticate(user=self.student)
        data = {"title": "Invalid Upload", "description": "Should not be allowed"}
        response = self.client.post(f"/api/sections/{self.section.id}/materials/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_materials(self):
        # Ensure materials can be retrieved
        MaterialFactory(section=self.section)
        response = self.client.get(f"/api/sections/{self.section.id}/materials/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)