<<<<<<< HEAD
from urllib import response
from accounts.models import User, Student
from home.models import Company, Job, InterviewExperience
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect , HttpResponseRedirect
=======
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from accounts.models import Student, User
from home.models import Job, Selection
from home import views 

>>>>>>> 80ca049b13e6c20c6f50e1acb3b996b991d52edc
# Create your views here.
def homeView(request):
    return render(request,'home/index.html')

<<<<<<< HEAD

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
=======
# Add a job/internship.... Only PRs can do
def addJob(request):
    print('here')
    if request.method == 'POST':
        try:
            student = User.objects.get(user=request.user)
            if student.isPR:
                description = request.POST['description']
                ctc = request.POST['ctc']
                profile = request.POST['profile']
                company = request.POST['company']
                location = request.POST['location']

                job = Job.objects.create(description=description, ctc=ctc, profile=profile, company=company, location=location, pr=student)
                job.save()

                messages.success(request, "Job Added Successfully!")
                return redirect(views.homeView)

            else:
                return HttpResponse('403 - Only PRs can post jobs')

        except:
            return HttpResponse('5XX - Some Error Occured')
    elif request.method == 'PUT':
        try:
            student = User.objects.get(user=request.user)
            if student.isPR:
                jobid = request.PUT['jobid']
                description = request.PUT['description']
                ctc = request.PUT['ctc']
                profile = request.PUT['profile']
                company = request.PUT['company']
                location = request.PUT['location']

                Job.objects.filter(id=jobid).update(description=description, ctc=ctc, profile=profile, company=company, location=location)

                messages.success(request, "Job Updated Successfully!")
                return redirect(views.homeView)

            else:
                return HttpResponse('403 - Only PRs can post jobs')

        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

# Open/Close are 2 states for job opening
def updateJobStatus(request):
    if request.method == 'POST':
        try:
            student = User.objects.get(user=request.user)
            if student.isPR:
                jobid = request.POST['jobid']
                open = request.POST['open']

                Job.objects.filter(id=jobid).update(open=open)

                messages.success(request, "Job Status Updated Successfully!")
                return redirect(views.homeView)

            else:
                return HttpResponse('403 - Only PRs can post jobs')

        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

# Update status of the candidate
def updateCandidateStatus(request):
    if request.method == 'POST':
        try:
            student = User.objects.get(user=request.user)
            if student.isPR:
                studentid = request.POST['studentid']
                selected = request.POST['selected']
                job = request.POST['job']

                Student.objects.filter(id=studentid).update(selected=selected)
                if selected:
                    Selection.objects.create(student=studentid, job=job)

                messages.success(request, "Student Status Updated Successfully!")
                return redirect(views.homeView)

            else:
                return HttpResponse('403 - Only PRs can update status of students')

        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def getData(request):
    return ""

def bookSlot(request):
    return ""
>>>>>>> 80ca049b13e6c20c6f50e1acb3b996b991d52edc
