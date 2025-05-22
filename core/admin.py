from django.contrib import admin
from .models import (
    User, Course, Section, CourseMaterial, Assignment,
    Submission, Chat, StatusUpdate, Feedback, Notification
)

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(CourseMaterial)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Chat)
admin.site.register(StatusUpdate)
admin.site.register(Feedback)
admin.site.register(Notification)