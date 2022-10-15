from urllib import response
from accounts.models import User, Student
from home.models import Company, Job, InterviewExperience, Selection, StudentJob
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect , HttpResponseRedirect
def profileView(request):
    data = {
        'Roll No.': '205121033',
        'Name': "Bhushan Mendhe",
        'email':"bmendhe23@gmail.com",
    }
    return render(request, 'student/profile.html', {'data': data.items()})

def resumeView(request):
    return render(request,'student/resume.html')

def companyView(request):
    return render(request,'student/companies.html')

def changePassword(request):
    return render(request,'student/changePassword.html')

def personalDetails(request):
    return render(request, 'student/personalDetails.html')