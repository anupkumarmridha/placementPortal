from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('/addJob', views.addJob, name='addJob'),
    path('/updateJobStatus', views.updateJobStatus, name='updateJobStatus'),
    ]