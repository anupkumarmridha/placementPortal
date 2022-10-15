from urllib import response
from accounts.models import User, Student
from home.models import Company, Job, InterviewExperience, Selection
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect , HttpResponseRedirect

from home import views 

# Create your views here.
def homeView(request):
    return render(request,'home/index.html')


#only by PR
def addCompany(request):
    if(request.method=='POST'):
        companyName=request.POST.get('companyName')
        companyType=request.POST.get('companyType')
        companyCategory=request.POST.get('companyCategory')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            if(student.isPR):
                company = Company(companyName=companyName, companyType=companyType, companyCategory=companyCategory)
                company.save()
                messages.success(request, "company successfully added!")
                return redirect('viewAllCompany')
            else:
                messages.error("Only PR can add company details!")

        except Exception as e:
            messages.success(request, "failed to add company!")
    else:
        return HttpResponse("404 - Not Found")


def updateCompany(request):
    if(request.method=='POST'):
        companyName=request.POST.get('companyName')
        companyType=request.POST.get('companyType')
        companyCategory=request.POST.get('companyCategory')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            company=Company.objects.filter(companyName=companyName)
            if(student.isPR):
                company = Company(companyName=companyName, companyType=companyType, companyCategory=companyCategory)
                company.save()
                messages.success(request, "company successfully updated")
                return redirect('viewAllCompany')
            else:
                messages.error("Only PR can add company details")

        except Exception as e:
            messages.success(request, "failed to add company")
        
    else:
        return HttpResponse("404 - Not Found")


def viewCompany(request,companyName):
    company=Company.objects.filter(companyName=companyName)
    

def viewAllCompany(request):
    companies=Company.objects.all()
    context={'companies':companies}
    #print(request.path_info)
    return HttpResponseRedirect(request.path_info, context)

def deleteCompany(request):
    pass

def addJob(request):
    if(request.method=='POST'):
        company=request.POST.get('company')
        role=request.POST.get('role')
        description=request.POST.get('description')
        ctc=request.POST.get('ctc')
        profile=request.POST.get('profile')
        location=request.POST.get('location')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            if(student.isPR):
                job = Job(company=company,role=role,description=description,ctc=ctc,profile=profile, location=location)
                job.save()
                messages.success(request, "Job successfully added!")
                return redirect('viewAllJob')
            else:
                messages.error("Only PR can add job details!")

        except Exception as e:
            messages.success(request, "failed to add job!")
    else:
        return HttpResponse("404 - Not Found")

def updateJob(request):
    if(request.method=='POST'):
        company=request.POST.get('company')
        role=request.POST.get('role')
        description=request.POST.get('description')
        ctc=request.POST.get('ctc')
        profile=request.POST.get('profile')
        location=request.POST.get('location')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            if(student.isPR):
                job = Job(company=company,role=role,description=description,ctc=ctc,profile=profile, location=location)
                job.save()
                messages.success(request, "Job successfully updated!")
                return redirect('viewAllJob')
            else:
                messages.error("Only PR can add job details!")

        except Exception as e:
            messages.success(request, "failed to add job!")
    else:
        return HttpResponse("404 - Not Found")

def viewJob(request):
    pass

def viewAllJob(request):
    jobs=Job.objects.all()
    context={'jobs':jobs}
    #print(request.path_info)
    return HttpResponseRedirect(request.path_info, context)

def deleteJob(request):
    pass


#all students
def addInterviewExperience(request):
    pass

def updateInterviewExperience(request):
    pass

def getInterviewExperience(request):
    pass


def getAllInterviewExperience(request):
    pass

def deleteInterviewExperience(request):
    pass
