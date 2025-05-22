from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Course, StatusUpdate, Feedback, Notification, CourseMaterial, Section, Assignment, Submission
from .serializers import *
from .tasks import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
import os
from django.shortcuts import redirect

User = get_user_model()

def index(request):
    return redirect("http://localhost:3000/")  # Redirect index to the Next.js frontend.  

# User Registration
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Returns user profile
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    include_courses = request.GET.get("include_courses", "false").lower() == "true"

    if include_courses:
        serializer = UserSerializer(request.user, context={"request": request})  # request context
    else:
        serializer = UserProfileSerializer(request.user, context={"request": request}) 
    
    return Response(serializer.data)

# Upload user profile picture
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_profile_picture(request):
    user = request.user
    
    if "profile_picture" not in request.FILES:
        return Response({"error": "No image file uploaded"}, status=400)

    user.profile_picture = request.FILES["profile_picture"]
    user.save()

    # Send a profile update notification (optional)
    send_profile_update_notification.delay(user.id)

    return Response({"message": "Profile picture updated successfully!", "profile_picture": user.profile_picture.url})

# Update user profile
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        send_profile_update_notification.delay(user.id)  # Send notification
        return Response({"message": "Profile updated successfully!"})

    return Response(serializer.errors, status=400)

# Course pagination (displays 9 courses per page)
class CoursePagination(PageNumberPagination):
    page_size = 12 
    page_size_query_param = "page_size"
    max_page_size = 50

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")  # Show latest courses first
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    filter_backends = [SearchFilter]  # Enable searching
    search_fields = ["title", "description"]  # Search by title or description

    # Allow teachers to remove students from a course
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def remove_student(self, request, pk=None):
        course = self.get_object()

        if request.user.role != "teacher":
            return Response({"error": "Only teachers can remove students."}, status=403)

        student_id = request.data.get("student_id")
        student = get_object_or_404(User, id=student_id, role="student")

        course.students.remove(student)
        return Response({"message": f"Student {student.username} removed from course."})
    
    # Filter courses based on query parameters
    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.all().order_by("-created_at")  # Default: all courses

        # If student: show enrolled courses
        if self.request.query_params.get("enrolled", None) == "true":
            return queryset.filter(students=user)

        # If teacher: show courses they teach
        if self.request.query_params.get("taught_by_me", None) == "true":
            return queryset.filter(teacher=user)

        return queryset
    
    # teachers can create courses
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def create_course(request):
        if request.user.role != "teacher":
            return Response({"error": "Only teachers can create courses."}, status=403)

        data = request.data.copy()
        data["teacher"] = request.user.id  # Ensure teacher is set

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class StatusUpdateViewSet(viewsets.ModelViewSet):
    queryset = StatusUpdate.objects.all().order_by("-created_at")
    serializer_class = StatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]

    # Assign user when updating status 
    def perform_create(self, serializer):
        status = serializer.save(user=self.request.user)
        # Send notification to all users
        self.notify_users(status)

    def notify_users(self, status):
        users = User.objects.all()  # Get all users

        notifications = [
            Notification(
                user=user,
                message=f"{status.user.username}: \"{status.content}\""
            )
            for user in users
        ]

        # Bulk create notifications for efficiency
        Notification.objects.bulk_create(notifications)

# Notifications ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by("-created_at")  # Order by latest
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]

    # Return notifications for specific authenticated user
    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user) 
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Course Enrollment
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user.is_anonymous:
        return Response({"error": "You must be logged in to enroll."}, status=401)

    course.students.add(request.user)

    # Trigger notification
    send_enrollment_notification.delay(course.id, request.user.id)

    return Response({"message": "Enrolled successfully!"})


# Course Update
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user)
    course.description = request.data.get("description", course.description)
    course.save()

    # Trigger notification
    send_course_update_notification.delay(course.id, "A course you are enrolled in has been updated.")

    return Response({"message": "Course updated and notifications sent."})


# Feedback ViewSet
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

# user searching
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def search(self, request):
        # search by username or email
        query = request.query_params.get("q", "")
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        # Optimize search with indexing & filters
        user = request.user
        if user.role == "teacher":
            results = User.objects.filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            ).distinct()
        else:  # Students can only search for teachers
            results = User.objects.filter(role="teacher").filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            ).distinct()

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
    

class CourseMaterialViewSet(viewsets.ModelViewSet):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        if self.request.user.role != "teacher":
            return Response({"error": "Only teachers can upload materials."}, status=403)
        material = serializer.save()
        # Notify students of newly uploaded material
        notify_students_of_material.delay(material.course.id)

# Teachers create course sections
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_section(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user)

    # Extract title and structure_type default = "custom"
    title = request.data.get("title")
    structure_type = request.data.get("structure_type", "custom")

    if not title:
        return Response({"error": "Section title is required."}, status=400)

    section = Section.objects.create(course=course, title=title, structure_type=structure_type)

    return Response(SectionSerializer(section).data, status=201)

# Allow teachers to upload & see materials
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_section_materials(request, section_id):
    section = get_object_or_404(Section, id=section_id)

    # Fetch all materials for this section
    if request.method == "GET":
        materials = CourseMaterial.objects.filter(section=section)
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)

    # Request to upload a new material
    if request.method == "POST":
        if request.user.role != "teacher":
            return Response({"error": "Only teachers can upload materials."}, status=403)

        title = request.data.get("title")
        description = request.data.get("description", "")
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "File is required."}, status=400)

        # Save the file temporarily
        temp_file_path = f"/tmp/{file.name}"
        with open(temp_file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Create Material Instance
        material = CourseMaterial.objects.create(
            section=section,
            title=title,
            description=description,
            uploaded_by=request.user
        )

        # Upload to Google Drive & Save Drive URL
        material.upload_to_drive(temp_file_path)

        # Remove local file after upload
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        return Response(MaterialSerializer(material).data, status=201)

# Students submit assignments
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    file_path = request.data.get("file_path")

    if not file_path:
        return Response({"error": "Missing file path"}, status=400)

    submission = Submission(assignment=assignment, student=request.user)
    submission.upload_to_drive(file_path)

    return Response({"message": "Homework submitted", "file_url": submission.file_url})


# View materials for all users
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_materials(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    materials = section.materials.all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)

# return all materials related to a course
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_course_materials(request, course_id):
    if request.method == "GET":
        # Correct the filtering by using sections related to the course
        materials = CourseMaterial.objects.filter(section__course_id=course_id)
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        if request.user.role != "teacher":
            return Response({"error": "Only teachers can upload materials."}, status=403)

        title = request.data.get("title")
        description = request.data.get("description", "")
        file = request.FILES.get("file")
        section_id = request.data.get("section_id")  # Get section ID

        if not file or not section_id:
            return Response({"error": "File and section ID are required."}, status=400)

        section = get_object_or_404(Section, id=section_id, course_id=course_id)
        material = CourseMaterial(section=section, title=title, description=description, file_url="google_drive_link", uploaded_by=request.user)
        material.upload_to_drive(file.temporary_file_path())
        
        return Response(MaterialSerializer(material).data, status=201)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_course_material(request, material_id):
    material = CourseMaterial.objects.get(id=material_id)
    if request.user.role != "teacher":
        return JsonResponse({"error": "Only teachers can delete materials."}, status=403)
    material.delete()
    return JsonResponse({"message": "Material deleted successfully!"})

# Get or create sections for course.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_course_sections(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "GET":
        sections = Section.objects.filter(course=course)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        if request.user.role != "teacher":
            return Response({"error": "Only teachers can create sections."}, status=403)

        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course)  # Assign section to the course
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
