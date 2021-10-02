from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
class HomeTestCase(TestCase):

    def test_courses_index(self):
        c = Client()
        response = c.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)