from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('addCompany', views.addCompany, name='addCompany'),
    path('addJob', views.addJob, name='addJob'),
    path('updateCompany/<int:pk>', views.addCompany, name='updateCompany'),
    path('companies', views.viewAllCompany, name='companies'),

    path('addInterviewExperience', views.addInterviewExperience, name='addInterviewExperience'),
    path('viewInterviewExperience', views.viewInterviewExperience, name='viewInterviewExperience'),
    path('viewDetailInterviewExperience/<int:pk>', views.viewDetailInterviewExperience, name='viewDetailInterviewExperience'),

    path('jobList', views.jobList, name='jobList'),
    path('updateJobStatus', views.updateJobStatus, name='updateJobStatus'),

    path('contactus', views.contactus, name='contactus'),

    ]