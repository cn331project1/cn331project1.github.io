from django.test import TestCase, Client
from .models import CourseModel
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.hashers import make_password
# Create your tests here.

class CourseTestCase(TestCase):
    
    def setUp(self):
        course1 = CourseModel.objects.create(code='CN000', name='test', semester=1, year=1, seat=1, status=True)
        student = User.objects.create(username='user1', password='1234')
    
    def test_courses_index(self):
        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_course(self):
        c = Client()
        course = CourseModel.objects.first()
        response = c.get(reverse('courses:course', args=(course.code,)))
        self.assertEqual(response.status_code, 200)

        