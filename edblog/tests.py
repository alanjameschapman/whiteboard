from django.test import TestCase
from django.contrib.auth.models import User
from .models import Teacher, School

# Create your tests here.
class TeacherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        School.objects.create(name='Test School')
        User.objects.create_user(username='testuser', password='12345')
        Teacher.objects.create(user=User.objects.get(username='testuser'), school=School.objects.get(name='Test School'))

    def test_teacher_content(self):
        teacher = Teacher.objects.get(id=1)
        expected_object_name = f'{teacher.user.username}'
        self.assertEquals(expected_object_name, 'testuser')