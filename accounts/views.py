from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse

from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from accounts.models import Student, PR, User
from django.contrib import messages
from home import views 
# Create your views here.
def handelSingup(request):
    if request.method =='POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user_type=request.POST.get('user_type')
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

"""
def handleLogin(request):
    if request.method !='POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)
            # messages.success(request, "Successfuly logged in 🥰")
            user_type = user.user_type
            print(user_type)
            #print("username : "+ request.POST.get("loginusername")+ "Password: " +request.POST.get("loginpassword"))
                
            if user_type == "1":
                # return HttpResponse("Student Login")
                return redirect(views.homeView)

            elif user_type == '2':
                customer_exist = Customer.objects.filter(user=user).exists()
                if customer_exist:
                    messages.success(request,f"Welcome {user.username} to Bid 'N Build !")
                    return redirect(views.homeView)

                return redirect('add_customer')

            elif user_type == '3':
                try:
                    company=Company.objects.get(user=user.id)
                    print(company.company_name)
                except:
                    pass
                
                company_exist = Company.objects.filter(user=user).exists()
                if company_exist:
                    messages.success(request,f"Welcome {company.company_name} to Bid 'N Build !")
                    return redirect(views.all_product_details)
                return redirect('add_company')
        else:
            messages.error(request, "Invalid credentialsl, Please try again 😎")
            return redirect(views.homeView)
"""