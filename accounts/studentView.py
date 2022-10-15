from django.urls import path
from accounts import studentView
from accounts.models import Student, User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse
from home import views
from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

def addStudentProfileDetails(request):
    if request.method=='POST':
        name=request.POST['name']
        roll=request.POST['roll']
        personalEmail=request.POST['personalEmail']
        dept=request.POST['dept']
        cgpa=request.POST['cgpa']
        phone=request.POST['phone']
        course=request.POST['course']
        graduationYear=request.POST['graduationYear']
        resume=request.POST['resume']
        profile_pic=request.POST['profile_pic']
        gender=request.POST['gender']
        homeAddress=request.POST['homeAddress']
        localAddress=request.POST['requestAddress']
        dob=request.POST['dob']
        isPR=False
        jobType=request.POST['jobType']
        fatherName=request.POST['fatherName']
        motherName=request.POST['motherName']
        guardianPhone=request.POST['guardianPhone']
        try:
            user=request.user
            mystudent = Student.objects.create_user(user=user,jobType=jobType,name=name,fatherName=fatherName,motherName=motherName,guardianPhone=guardianPhone, personalEmail=personalEmail,dept=dept,cgpa=cgpa,phone=phone,course=course, graduationYear=graduationYear,resume=resume,profile_pic=profile_pic,isPR=isPR,gender=gender,dob=dob,homeAddress=homeAddress, localAddress=localAddress,roll=roll  ) 
            mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect('home')
    else:
        return HttpResponse("404 - Not Found")

def updateStudentProfileDetails(request):
    pass
