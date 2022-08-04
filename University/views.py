
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import models

from .models import OfferedCourse, Grade, CourseRegistrations

from . import courseadd
from .import studentRegistration


# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def login(request):
    if request.method=='POST':
        username=request.POST['id']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('University:menu')
        else:
            messages.info(request,'Credentials given are wrong')
            return redirect('University:login')
    else:
        return render(request,'login.html')

def signUp(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['id']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('University:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'ID already exists')
                return redirect('University:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                student=studentRegistration.StudentAdd(username,fullname,email)
                student.addStudent()
                return redirect('University:login')
                


        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('University:signup')
    else:
         return render(request, 'sign_up.html')
     
@login_required
def menu(request):
    return render(request,"menu.html")

@login_required
def course_add(request):
    if request.method=='POST':
        course_id=request.POST['courseID']
        name=request.POST['courseName']
        description=request.POST['description']
        student_id = request.user.id
        course=courseadd.CourseAdd(course_id,name,description,student_id)
        course.addCourse()
    return render(request, 'course_add.html')

@login_required
def course_drop(request):
    if request.method=='POST':
        id=request.POST['courseID']
        course=courseadd.CourseAdd(id)
        course.deleteCourse()
    
    return render(request,'course_drop.html')

@login_required
def course_registration(request):
    data = serializers.serialize("python",OfferedCourse.objects.all())
    context = {
        'data':data,
    }
    return render(request, 'course_registration.html', context)

@login_required
def personal_information(request):
    courses = CourseRegistrations.objects.filter(owner=request.user)
    context = {'courses':courses}
    return render(request, 'personal_information.html',context)

@login_required
def results(request):
    grades = Grade.objects.filter(owner=request.user).order_by('date_added')
    context = {'grades':grades}
    return render(request, 'results.html',context)

