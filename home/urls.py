from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('addCompany', views.addCompany, name='addCompany'),
    path('updateCompany/<int:pk>', views.addCompany, name='updateCompany'),
    path('companies', views.viewAllCompany, name='companies'),

    path('updateJobStatus', views.updateJobStatus, name='updateJobStatus'),
    ]