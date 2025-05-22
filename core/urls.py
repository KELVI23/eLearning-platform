from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

# Register ViewSets in Router
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'statuses', StatusUpdateViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'users', UserViewSet)
router.register(r'materials', CourseMaterialViewSet)
  

urlpatterns = [
    path('', include(router.urls)), # rest api root
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("courses/<int:course_id>/enroll/", enroll_course, name="enroll-course"),
    path("courses/<int:course_id>/update/", update_course, name="update-course"),
    path("courses/<int:course_id>/materials/", get_course_materials, name="get_course_materials"),
    path("courses/<int:course_id>/sections/", get_course_sections, name="get_course_sections"),
    path("materials/<int:material_id>/delete/", delete_course_material, name="delete_course_material"),
    path("courses/<int:course_id>/sections/", create_section, name="create_section"),
    path("sections/<int:section_id>/materials/", get_section_materials, name="get_section_materials"),
    path("sections/<int:section_id>/materials/view/", get_materials, name="get_materials"),
    path("assignments/<int:assignment_id>/submissions/", submit_assignment, name="submit_assignment"),
    path("profile/", user_profile, name="user_profile"),
    path("account/update/", update_profile, name="update_profile"),
    path("account/upload-profile-picture/", upload_profile_picture, name="upload_profile_picture"),

    # API schema and docs
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)