from celery import shared_task
from .models import Notification, User, Course, CourseMaterial
# from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_course_update_notification(course_id, message):
    students = User.objects.filter(enrolled_courses__id=course_id)
    for student in students:
        Notification.objects.create(user=student, message=message)
    return "Notifications sent successfully!"

# Notify students when course is updated
@shared_task
def send_course_update_notification(course_id, message):
    try:
        course = Course.objects.get(id=course_id)
        students = course.students.all()
        for student in students:
            Notification.objects.create(user=student, message=message)

        return "Notifications sent successfully!"
    except Course.DoesNotExist:
        return "Course not found."

# Notify teacher when student enrolls
@shared_task
def send_enrollment_notification(course_id, student_id):
    try:
        course = Course.objects.get(id=course_id)
        student = User.objects.get(id=student_id)

        Notification.objects.create(
            user=course.teacher,
            message=f"{student.username} has enrolled in your course '{course.title}'."
        )

        return "Enrollment notification sent!"
    except Course.DoesNotExist:
        return "Course not found."

# Notify students when new course material is uploaded
@shared_task
def notify_students_of_material(material_id):
    try:
        material = CourseMaterial.objects.get(id=material_id)
        course = material.section.course
        students = course.students.all()

        for student in students:
            Notification.objects.create(
                user=student, 
                message=f"New material '{material.title}' has been added to the course '{course.title}'."
            )

        return "Material upload notifications sent!"
    except CourseMaterial.DoesNotExist:
        return "Material not found."

# Notify user when their profile is updated
@shared_task
def send_profile_update_notification(user_id):
    user = User.objects.get(id=user_id)
    Notification.objects.create(
        user=user,
        message="Your profile has been updated successfully!"
    )

# Notify user when their password is changed
@shared_task
def send_password_change_notification(user_id):
    user = User.objects.get(id=user_id)
    Notification.objects.create(
        user=user,
        message="Your password has been changed successfully!"
    )