import factory
from django.contrib.auth import get_user_model
from core.models import Course, Feedback, CourseMaterial, Section

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    # Factory for creating User objects
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "testpass")
    role = factory.Iterator(["student", "teacher"])

class CourseFactory(factory.django.DjangoModelFactory):
    # Factory for creating Course objects
    class Meta:
        model = Course

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")
    teacher = factory.SubFactory(UserFactory, role="teacher")

class FeedbackFactory(factory.django.DjangoModelFactory):
    # Factory for creating Feedback objects
    class Meta:
        model = Feedback

    student = factory.SubFactory(UserFactory, role="student")
    course = factory.SubFactory(CourseFactory)
    rating = factory.Iterator([1, 2, 3, 4, 5])
    comment = factory.Faker("sentence")

class SectionFactory(factory.django.DjangoModelFactory):
    # Factory for creating Section objects
    class Meta:
        model = Section

    course = factory.SubFactory(CourseFactory)
    title = factory.Faker("sentence", nb_words=2)
    structure_type = "custom"

class MaterialFactory(factory.django.DjangoModelFactory):
    # Factory for creating CourseMaterial objects
    class Meta:
        model = CourseMaterial

    section = factory.SubFactory(SectionFactory)
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text")
    file_url = "https://example.com/material.pdf"
    file_type = "pdf"