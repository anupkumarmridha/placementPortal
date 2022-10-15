from urllib import response
from accounts.models import User, Student
from home.models import Company, Job, InterviewExperience, Selection, StudentJob
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect , HttpResponseRedirect
from home.forms import addCompanyForm, updateCompanyForm
from home import views 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# Create your views here.
def homeView(request):
    return render(request,'home/index.html')



#only by PR
def addCompany(request):
    
    if request.method=='POST':
        
        try:
            user=request.user
            student=Student.objects.get(user=user)
            if(student.isPR):
                form=addCompanyForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Company info added successfully")
                    return redirect('homeView')
                else:
                    messages.error(request, "Form is Not Valid")
        except Exception as e:
            print(e)
    else:
        form=addCompanyForm()
    context={
        'form':form
        }
    return render(request,'home/addCompany.html',context=context)

class updateCompany(UpdateView):
    model=Company
    form_class=updateCompanyForm
    template_name='home/updateCompany.html'
    def get_success_url(self):
        return reverse( 'homeView')


# def addCompany(request):
#     if(request.method=='POST'):
#         companyName=request.POST.get('companyName')
#         companyType=request.POST.get('companyType')
#         companyCategory=request.POST.get('companyCategory')
#         try:
#             user=request.user
#             student=Student.objects.get(user=user)
#             if(student.isPR):
#                 company = Company(companyName=companyName, companyType=companyType, companyCategory=companyCategory)
#                 company.save()
#                 messages.success(request, "company successfully added!")
#                 return redirect('viewAllCompany')
#             else:
#                 messages.error("Only PR can add company details!")

#         except Exception as e:
#             messages.success(request, "failed to add company!")
#     else:
#         return HttpResponse("404 - Not Found")


# def updateCompany(request):
#     if(request.method=='POST'):
#         companyName=request.POST.get('companyName')
#         companyType=request.POST.get('companyType')
#         companyCategory=request.POST.get('companyCategory')
#         try:
#             user=request.user
#             student=Student.objects.get(user=user)
#             company=Company.objects.filter(companyName=companyName)
#             if(student.isPR):
#                 company = Company(companyName=companyName, companyType=companyType, companyCategory=companyCategory)
#                 company.save()
#                 messages.success(request, "company successfully updated")
#                 return redirect('viewAllCompany')
#             else:
#                 messages.error("Only PR can add company details")

#         except Exception as e:
#             messages.success(request, "failed to add company")
        
#     else:
#         return HttpResponse("404 - Not Found")


def viewCompany(request,companyName):
    company=Company.objects.filter(companyName=companyName)
    

def viewAllCompany(request):
    companies=Company.objects.all()
    context={'companies':companies}
    #print(request.path_info)
    return render(request,'home/companies.html',context=context)

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

def updateJobStatus(request):
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
    if request.method == 'GET':
        id = request.GET.get('q', '')
        try:
            job = Job.objects.filter(id=id)
            return HttpResponse(job)
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')

def viewAllJob(request):
    jobs=Job.objects.all()
    context={'jobs':jobs}
    #print(request.path_info)
    return HttpResponseRedirect(request.path_info, context)

def deleteJob(request):
    if request.method == 'DELETE':
        id = request.GET.get('q', '')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            if student.isPR == False:
                return HttpResponse('403 - Only PRs can delete Jobs')
            Job.objects.filter(id=id).delete()
            return HttpResponse('Deleted Successfully')
        except:
            return HttpResponse('5XX - Some Error Occured')
    else:
        return HttpResponse('404 - NOT FOUND')


#all students
def interviewExperience(request):
    if request.method=='POST':
        company=request.POST.get('company')
        experience=request.POST.get('experience')
        jobProfile=request.POST.get('jobProfile')
        try:
            user=request.user
            student=Student.objects.get(user=user)
            interviewExperience = InterviewExperience(company=company,jobProfile=jobProfile,experience=experience,user=student)
            interviewExperience.save()
            messages.success(request, "Job successfully added!")
            return redirect('getAllInterviewExperience')

        except Exception as e:
            messages.success(request, "failed to add job!")
    elif request.method=='PUT':
        company=request.PUT.get('company')
        experience=request.PUT.get('experience')
        jobProfile=request.PUT.get('jobProfile')
        id=request.PUT['id']
        try:
            user=request.user
            student=Student.objects.get(user=user)
            interview = InterviewExperience.objects.filter(id=id)
            if interview.user != user:
                messages.success(request, "You are unauthorized")
                return HttpResponse("403 - Unauthorized Access")
            interview.update(company=company,jobProfile=jobProfile,experience=experience,user=student)
            interview.save()
            messages.success(request, "Job successfully updated!")
            return redirect('getAllInterviewExperience')

        except Exception as e:
            messages.success(request, "failed to add job!")
    elif request.method == 'GET':
        id = request.GET.get('q', '')
        try:
            interview = InterviewExperience.objects.filter(id=id)
            return HttpResponse(interview)
        except:
            return HttpResponse('Some Error Occured')
    elif request.method == 'DELETE':
        id = request.GET.get('q', '')
        try:
            InterviewExperience.objects.filter(id=id).delete()
            return HttpResponse('Deleted Successfully')
        except:
            return HttpResponse('Some Error Occured')
    else:
        return HttpResponse("404 - Not Found")


def getAllInterviewExperience(request):
    if request.method == 'GET':
        try:
            interviews = InterviewExperience.objects.all()
            return HttpResponse(interviews)
        except:
            return HttpResponse('Some Error occured')
    else:
        return HttpResponse('404 - Not Found')    

# add in studentJob
def addStudentJob(request):
    if request.method == 'POST':
        job = request.POST['job']
        student = request.POST['student']
        round = request.POST['round']
        try:
            user=request.user
            stu=Student.objects.get(user=user)
            if stu.isPR==False:
                return HttpResponse('403 - Unauthorized')
            studentJob = StudentJob.objects.create(job=job, student=student, round=round)
            return HttpResponse(studentJob)
        except:
            return HttpResponse('Some Error Occured')
    elif request.method == 'PUT':
        job = request.PUT['job']
        student = request.PUT['student']
        round = request.PUT['round']
        status = request.PUT['status']
        try:
            user=request.user
            stu=Student.objects.get(user=user)
            if stu.isPR==False:
                return HttpResponse('403 - Unauthorized')
            studentJob = StudentJob.objects.filter(job=job, student=student, round=round).update(status=status)
            if status == 'Selected':
                Selection.objects.create(student=student, job=job)
            return HttpResponse(studentJob)
        except:
            return HttpResponse('Some Error Occured')
    else:
        return HttpResponse('404 - Not Found')



#Placement Status for students
#Company -> open / closed, JD, registration link, upload resume/download resume

#PR-> Company -> convince close /open PPT OT PI time slot venue shortlisted candidates selected candidates 
#csv file for the students who attempted OT