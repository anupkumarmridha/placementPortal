from logging import exception
from django.urls import path
from accounts import studentView
from accounts.models import Student, User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse
from home import views
from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

def addAdditionalDetails(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        personalEmail = request.POST["personalEmail"]
        gender = request.POST["gender"]
        if len(request.FILES) != 0:
            profile_pic=request.FILES['profile_pic']
            print(profile_pic)
        else:
            profile_pic=None
        dob = request.POST["dob"]
        homeAddress = request.POST["homeAddress"]
        jobType = request.POST["jobType"]
        localAddress = request.POST["localAddress"]
        fatherName = request.POST["fatherName"]
        motherName = request.POST["motherName"]
        guardianPhone = request.POST["guardianPhone"]
        roll = request.user.username
        degreeLevel = request.POST["degreeLevel"]
        currentDept = request.POST["currentDept"]
        currentCourse = request.POST["currentCourse"]
        currentCgpa = request.POST["currentCgpa"]
        currentCourseGraduationYear = request.POST["currentCourseGraduationYear"]
        class10Percentage = request.POST["class10Percentage"]
        class12Percentage = request.POST["class12Percentage"]
       
        ugDegree = request.POST["ugDegree"]
        ugCgpa = request.POST["ugCgpa"]
        ugCollege = request.POST["ugCollege"]
        ugGraduationYear = request.POST["ugGraduationYear"]
    
        try:
            user = request.user

            mystudent = Student.objects.create(
                user=user,
                jobType=jobType,
                fatherName=fatherName,
                motherName=motherName,
                guardianPhone=guardianPhone,
                personalEmail=personalEmail,
                phone=phone,
                profile_pic=profile_pic,
                gender=gender,
                dob=dob,
                homeAddress=homeAddress,
                localAddress=localAddress,
                roll=roll,
                degreeLevel=degreeLevel,
                currentDept=currentDept,
                currentCourse=currentCourse,
                currentCgpa=currentCgpa,
                currentCourseGraduationYear=currentCourseGraduationYear,
                class10Percentage=class10Percentage,
                class12Percentage=class12Percentage,
                ugDegree=ugDegree,
                ugCgpa=ugCgpa,
                ugCollege=ugCollege,
                ugGraduationYear=ugGraduationYear,
            )
            mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except Exception as e:
            print(e)
            messages.error(request, "Failed to add Details!")

            return redirect(views.homeView)
    else:
        messages.error(request, "404 Not Found")
    return render(request, "student/studentDashboard.html")

def viewStudentProfile(request):
    try:
        user=request.user
        studentProfile = Student.objects.filter(user=user)
        context={
        'studentDetails': studentProfile
        }
        return render(request, "student/studentDashboard.html", context)
    except Exception as e:
        messages.error(request, "Student profile not found")
        print(e)
    return render(request, "student/studentDashboard.html")

def updateResume(request):
    if request.method=='POST':
        if len(request.FILES) != 0:
            resume=request.FILES['resume']
        else:
            resume=None
        try:
            user=request.user
            student=Student.objects.get(user=user)
            student.resume=resume

            student.save()
            messages.success(request, "Resume Updated Successfully")
        except Exception as e:
            print(e)
            messages.error(request, "EducationDetails Not Found")
        return redirect(views.homeView)

    return render(request,'student/resume.html')
