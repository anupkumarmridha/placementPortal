from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse

from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from accounts.models import Student, User
from django.contrib import messages
from home import views 
from home.models import Job, Selection
from datetime import datetime, timedelta
# Create your views here.

def admin_home(request):
    pass

def handelSingup(request):
    if request.method =='POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        webMail= username+'@nitt.edu'
        email = webMail
        # email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user_type='2'
        #check for errorneous input
        print(user_type)

        if pass1 != pass2 :
            messages.error(request, "Password do not match.")
            return redirect('handelSingup')    

        #Create User
        
        try:
            myuser = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname, user_type=user_type)

            myuser.save()
            messages.success(request, "Account Created Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect('home')
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method !='POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginusername=loginusername+'@nitt.edu'
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)      
        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly logged in 🥰")
        else:
            messages.error(request, "Invalid credentialsl, Please try again 😎")
            return redirect(views.homeView)

def handleLogout(request):
    if request.method=='POST':
        value=request.POST['value']
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")
        
        return redirect(views.homeView)
    else:
        return HttpResponse('Sorry No Users Logged in 😎') 

# To add or update resume
def addResume(request):
    if request.method == 'POST':
        resume = request.POST['resume']
        try:
            Student.objects.filter(id=request.user).update(resume=resume)
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def updateDetails(request):
    if request.method == 'POST':
        dept = request.POST['dept']
        course = request.POST['course']
        graduationYear = request.POST['graduationYear']
        cgpa = request.POST['cgpa']
        gender = request.POST['gender']
        profile_pic = request.POST['profile_pic']
        phone = request.POST['phone']
        dob = request.POST['dob']
        homeAddress = request.POST['homeAddress']
        localAddress = request.POST['localAddress']
        try:
            Student.objects.filter(id=request.user).update(dept=dept, course=course, graduationYear=graduationYear, cgpa=cgpa, gender=gender, profile_pic=profile_pic, phone=phone, dob=dob, homeAddress=homeAddress, localAddress=localAddress)
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def updatePassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        newPassword = request.POST['newPassword']
        verifyPassword = request.POST['verifyPassword']
        if newPassword != verifyPassword:
            return HttpResponse('403 - Passwords do not match')
        try:
            success = Student.check_password(password)
            if success:
                Student.objects.get(id=request.user).set_password(newPassword)
            else:
                return HttpResponse('403 - Incorrect Password')
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def getJobListing(request):
    if request.method == 'GET':
        try:
            last2month = datetime.today() - timedelta(days=60)
            jobs = Job.objects.filter(created_at__gte=last2month).order_by('created_at')
            return HttpResponse(jobs)
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def getJD(request):
    if request.method == 'GET':
        id = request.GET.get('q', '')
        try:
            job = Job.objects.filter(id=id)
            return HttpResponse(job)
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')