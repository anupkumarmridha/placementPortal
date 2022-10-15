from django.shortcuts import render, HttpResponse, redirect

from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from accounts.models import Student, User
from django.contrib import messages
from home import views

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from typing import Protocol

# Create your views here.

from .tokens import account_activation_token


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("handleLogin")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect(views.homeView)


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string(
        "template_activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f"Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.",
        )
    else:
        messages.error(
            request,
            f"Problem sending email to {to_email}, check if you typed it correctly.",
        )


def admin_home(request):
    pass


def handelSingup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        webMail = username + "@nitt.edu"
        email = webMail
        # email = request.POST['email']
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        user_type = "2"
        # check for errorneous input
        print(user_type)

        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect("handelSingup")

        # Create User

        try:
            myuser = User.objects.create_user(
                username=username,
                password=pass1,
                email=email,
                first_name=fname,
                last_name=lname,
                user_type=user_type,
            )
            myuser.is_active = False
            myuser.save()
            
            # print("here")
            activateEmail(request, myuser, email)
            messages.success(request, "Account Created Successfully!")
            return redirect(views.homeView)

        except Exception as e:
            print(e)
            messages.error(request, "Failed to SignUp!")
            return redirect(views.homeView)
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method != "POST":
        return HttpResponse("Submission outside this window is not allowed 😎")
    else:
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginusername = loginusername + "@nitt.edu"
        loginpassword = request.POST["loginpassword"]
        user = EmailBackEnd.authenticate(
            request, username=loginusername, password=loginpassword
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly logged in 🥰")
            return redirect(views.homeView)
        else:
            messages.error(request, "Invalid credentialsl, Please try again 😎")
            return redirect(views.homeView)


def handleLogout(request):
    if request.method == "POST":
        value = request.POST["value"]
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")

        return redirect(views.homeView)
    else:
        return HttpResponse("Sorry No Users Logged in 😎")
