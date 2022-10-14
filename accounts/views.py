from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse

from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from accounts.models import Student, User
from django.contrib import messages
from home import views 
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
            return redirect(views.homeView)
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