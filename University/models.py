from distutils.archive_util import make_zipfile
from operator import mod
from pickle import FALSE
from statistics import mode
from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import User

# Create your models here.

class OfferedCourse(models.Model):
    id=models.CharField(max_length=50,primary_key=True,null=False,blank=False,verbose_name="Course ID")
    name=models.CharField(max_length=100,null=False,blank=False,verbose_name="Course Name")
    description=models.CharField(max_length=150,null=False,blank=True,verbose_name="Description")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentList(models.Model):
    id=models.CharField(max_length=20,primary_key=True,null=False,blank=FALSE,verbose_name="Student Id")
    fullname=models.CharField(max_length=50,null=False,verbose_name="Full Name")
    email=models.CharField(max_length=50,null=False,verbose_name="Email")


class Grade(models.Model):
    course_id=models.CharField(max_length=20,null=False,blank=FALSE,verbose_name="Course Id")
    result=models.CharField(max_length=50,null=False,verbose_name="Result")
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class CourseRegistrations(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course_ID=models.CharField(max_length=50,null=False,verbose_name="Course ID")
    course_Name=models.CharField(max_length=50,null=False,verbose_name="Course Name")
    course_Description=models.CharField(max_length=50,null=False,verbose_name="Course Description")
