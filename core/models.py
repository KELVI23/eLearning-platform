from django.contrib.auth.models import AbstractUser
from django.db import models
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os

# Google Drive API Setup
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
SERVICE_ACCOUNT_FILE = "core/env/exampleKey.json" # replace with actual key and folder
PARENT_FOLDER_ID = "folder"  # Google Drive Folder ID

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build("drive", "v3", credentials=credentials)

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    students = models.ManyToManyField(User, related_name="enrolled_courses", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)  
    difficulty_level = models.CharField(max_length=50, default="All Levels")  

    def __str__(self):
        return self.title

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat from {self.sender} to {self.receiver}"
    
class StatusUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="statuses")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
    
class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="feedback")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student} for {self.course.title}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

# sections within course material
class Section(models.Model):
    STRUCTURE_CHOICES = [
        ("week", "Week"),
        ("chapter", "Chapter"),
        ("custom", "Custom"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)
    structure_type = models.CharField(max_length=50, choices=STRUCTURE_CHOICES)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
class CourseMaterial(models.Model):
    FILE_TYPE_CHOICES = [
        ("video", "Video"),
        ("pdf", "PDF"),
        ("image", "Image"),
        ("zip", "ZIP"),
        ("other", "Other"),
    ]

    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="materials", null=True, blank=True)
    title = models.CharField(max_length=255, default="Untitled Material", blank=False)
    description = models.TextField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)  # Store Google Drive link
    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES, default="other")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Upload file to Google Drive & save link in the database
    def upload_to_drive(self, file_path):
        file_metadata = {
            "name": os.path.basename(file_path),
            "parents": [PARENT_FOLDER_ID],
        }
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields="id,webViewLink").execute()
        self.file_url = file.get("webViewLink")
        self.save()

# student assignment request
class Assignment(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=255)
    prompt = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.section.course.title} - {self.title}"

# student assignment submission
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file_url = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def upload_to_drive(self, file_path):
        file_metadata = {
            "name": os.path.basename(file_path),
            "parents": [PARENT_FOLDER_ID],
        }
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields="id,webViewLink").execute()
        self.file_url = file.get("webViewLink")
        self.save()