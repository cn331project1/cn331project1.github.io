
from django.http import request
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.hashers import make_password

# Create your tests here.

class UserViewIndexTestCase(TestCase):
    
    def setUp(self):
        pwd = make_password('password')
        user1 = User.objects.create(username='user1', password=pwd , email='user1@email.com')
        
    def test_index_view(self):
        c = Client()
        c.force_login(User.objects.first())
        res = c.get(reverse('users:index'))
        self.assertEqual(res.status_code, 200)

    def test_index_view_no_authenciation(self):
        c = Client()
        res = c.get(reverse('users:index'))
        self.assertEqual(res.status_code, 302)

    def test_login_view_success(self):
        c = Client()  
        data = {'username': 'user1', 'password': 'password'}   
        res = c.post(reverse('users:login'), data , follow = True)         
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'users/index.html')
    
    def test_login_view_unsuccess(self):
        c = Client()  
        data = {'username': 'user1', 'password': '1234'}   
        res = c.post(reverse('users:login'), data , follow = True)         
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'users/login.html')
    
    def test_logout_view(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse('users:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')