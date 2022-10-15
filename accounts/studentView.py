from django.urls import path
from accounts import studentView
from accounts.models import EducationDetails, Student, User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse
from home import views
from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout


def addStudentBasicProfileDetails(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        personalEmail = request.POST["personalEmail"]
        gender = request.POST["gender"]
        profile_pic = request.POST["profile_pic"]
        dob = request.POST["dob"]
        homeAddress = request.POST["homeAddress"]
        jobType = request.POST["jobType"]
        localAddress = request.POST["requestAddress"]
        fatherName = request.POST["fatherName"]
        motherName = request.POST["motherName"]
        guardianPhone = request.POST["guardianPhone"]

        try:
            user = request.user
            mystudent = Student.objects.create_user(
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
            )
            mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect("home")
    else:
        messages.error(request, "404 Not Found")
    return render(request, "student/addBasicDetails.html")


def updateStudentBasicProfileDetails(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        personalEmail = request.POST["personalEmail"]
        gender = request.POST["gender"]
        profile_pic = request.POST["profile_pic"]
        dob = request.POST["dob"]
        homeAddress = request.POST["homeAddress"]
        jobType = request.POST["jobType"]
        localAddress = request.POST["requestAddress"]
        fatherName = request.POST["fatherName"]
        motherName = request.POST["motherName"]
        guardianPhone = request.POST["guardianPhone"]

        try:
            user = request.user
            mystudent = Student.objects.filter(user=user)
            mystudent.update(
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
            )
            mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect("home")
    else:
        messages.error(request, "404 Not Found")
    return render(request, "student/updateBasicDetails.html")


def addStudentEducationProfileDetails(request):
    if request.method == "POST":
        roll = request.user.username
        degreeLevel = request.POST["degreeLevel"]
        currentDept = request.POST["currentDept"]
        currentCourse = request.POST["currentCourse"]
        currentCgpa = request.POST["currentCgpa"]
        currentCourseGraduationYear = request.POST["currentCourseGraduationYear"]
        class10Percentage = request.POST["class10Percentage"]
        class12Percentage = request.POST["class12Percentage"]
        if degreeLevel == "PG":
            ugDegree = request.POST["ugDegree"]
            ugCgpa = request.POST["ugCgpa"]
            ugCollege = request.POST["ugCollege"]
            ugGraduationYear = request.POST["ugGraduationYear"]
        resume = request.POST["resume"]

        try:
            user = request.user
            if degreeLevel == "PG":
                mystudent = EducationDetails.objects.create_user(
                    student=user,
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
                    resume=resume,
                )
                mystudent.save()
            else:
                mystudent = EducationDetails.objects.create_user(
                    student=user,
                    roll=roll,
                    degreeLevel=degreeLevel,
                    currentDept=currentDept,
                    currentCourse=currentCourse,
                    currentCgpa=currentCgpa,
                    currentCourseGraduationYear=currentCourseGraduationYear,
                    class10Percentage=class10Percentage,
                    class12Percentage=class12Percentage,
                    resume=resume,
                )
                mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect("home")
    else:
        messages.error(request, "404 Not Found")
    return render(request, "student/addBasicDetails.html")



def updateStudentEducationProfileDetails(request):
    if request.method == "POST":
        roll = request.user.username
        degreeLevel = request.POST["degreeLevel"]
        currentDept = request.POST["currentDept"]
        currentCourse = request.POST["currentCourse"]
        currentCgpa = request.POST["currentCgpa"]
        currentCourseGraduationYear = request.POST["currentCourseGraduationYear"]
        class10Percentage = request.POST["class10Percentage"]
        class12Percentage = request.POST["class12Percentage"]
        if degreeLevel == "PG":
            ugDegree = request.POST["ugDegree"]
            ugCgpa = request.POST["ugCgpa"]
            ugCollege = request.POST["ugCollege"]
            ugGraduationYear = request.POST["ugGraduationYear"]
        resume = request.POST["resume"]

        try:
            student=Student.objects.filter(user=request.user)
            if degreeLevel == "PG":
                
                mystudent = EducationDetails.objects.filter(student=student)
                mystudent = mystudent.update(
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
                    resume=resume,
                )
                mystudent.save()
            else:
                student=Student.objects.filter(user=request.user)
                mystudent = EducationDetails.objects.filter(student=student)
                mystudent = mystudent.update(
                    roll=roll,
                    degreeLevel=degreeLevel,
                    currentDept=currentDept,
                    currentCourse=currentCourse,
                    currentCgpa=currentCgpa,
                    currentCourseGraduationYear=currentCourseGraduationYear,
                    class10Percentage=class10Percentage,
                    class12Percentage=class12Percentage,
                    resume=resume,
                )
                mystudent.save()
            messages.success(request, "Student details updated Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect("home")
    else:
        messages.error(request, "404 Not Found")
    return render(request, "student/addBasicDetails.html")

def viewStudentProfile(request):
    try:
        user=request.user
        studentProfile = Student.objects.filter(user=user)
        student=Student.objects.get(user=request.user)
        StudentEducationDetails = EducationDetails.objects.filter(student=student)
        context={
        'details': list(studentProfile.values()) + list(StudentEducationDetails.values())
    }
        print(context['details'])
        return render(request, "student/viewStudentProfile.html", context)
    except:
        messages.error(request, "Student profile not found")
    return render(request, "student/viewStudentProfile.html")

def updateResume(request):
    return render(request,'student/resume.html')
