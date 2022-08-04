from cgi import print_arguments
from http import client
from multiprocessing.connection import Client
from turtle import home
from urllib import response
from django.test import SimpleTestCase, TestCase
from django.urls import reverse,resolve
import json
from University.models import StudentList,OfferedCourse

from University.views import homepage, login

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url=reverse('University:homepage')
        self.assertEqual(resolve(url).func,homepage)
        
    def test_list_url_is_resolved(self):
        url=reverse('University:login')
        self.assertEqual(resolve(url).func,login)
class TestViews(TestCase):
    #doesn't work
    def test_call_view_load(self):
        self.client.login(username='user', password='pass')  # defined in fixture or with factory in setUp()
        response = self.client.get('University:menu')
        self.assertEqual(response.status_code, 404)
        

class testModels(TestCase):
    def setUp(self):
        self.studnet1=StudentList.objects.create(
            id='29',
            fullname='student1',
            email="ungabunga"
            
        )      
    def test_student_list_working(self):
        self.assertNotEqual(self.studnet1,"29")
