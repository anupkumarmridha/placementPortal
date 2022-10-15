from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from accounts.models import Student, User
from home.models import Job, Selection
from home import views 

# Create your views here.
def homeView(request):
    return render(request,'home/index.html')

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