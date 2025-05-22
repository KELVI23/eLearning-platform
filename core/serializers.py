from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course, Feedback, StatusUpdate, Notification, Section, CourseMaterial, Assignment, Submission
from django.contrib.auth.hashers import make_password

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]  

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])  # Hash password
        user = User.objects.create(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    enrolled_courses = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "profile_picture", "enrolled_courses"]

    # Return enrolled courses
    def get_enrolled_courses(self, obj):
        if hasattr(obj, "enrolled_courses"):
            return CourseSerializer(obj.enrolled_courses.all(), many=True).data
        return []

    # Returns URL for profile pictures
    def get_profile_picture(self, obj):
        request = self.context.get("request")  # Get the request context

        if obj.profile_picture:
            if request:
                return request.build_absolute_uri(f"/api/media/{obj.profile_picture}")
            return f"/api/media/{obj.profile_picture}"  # Fallback URL
        return None  # No profile picture

class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()  # Show teacher's name
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())   # Show enrolled students

    class Meta:
        model = Course
        fields = ["id", "title", "description", "teacher", "students", "image_url", "difficulty_level"]

class StatusUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")  # Automatically assign user

    class Meta:
        model = StatusUpdate
        fields = ["id", "user", "content", "created_at"]

class FeedbackSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.username")  # Prevent needing student in request

    class Meta:
        model = Feedback
        fields = ['id', 'student', 'course', 'rating', 'comment', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "user", "message", "is_read", "created_at"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture']

# User profile updates
class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)
    
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ["id", "title", "structure_type", "course"]
        read_only_fields = ["course"]  # Ensure course is not required in input

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"