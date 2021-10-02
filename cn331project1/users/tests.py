
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.hashers import make_password

# Create your tests here.

class UserViewIndexTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(username='user1', password='1234', email='user1@email.com')

    def test_index_view(self):
        c = Client()
        user = User.objects.get(username='user1', password='1234', email='user1@email.com')
        c.force_login(user)
        res = c.get(reverse('users:index'))
        self.assertEqual(res.status_code, 200)

    def test_index_view_no_authenciation(self):
        c = Client()
        user = User.objects.get(username='user1', password='1234', email='user1@email.com')
        res = c.get(reverse('users:index'))
        self.assertEqual(res.status_code, 302)

    
class UserViewloginTestCase(TestCase):
    pass
