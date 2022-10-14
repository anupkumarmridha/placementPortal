from django.urls import path
from accounts import views

urlpatterns = [
  path('/signup/', views.handelSingup, name='handelSingup'),

  path('/login', views.handleLogin, name='handleLogin'),
  path('/logout', views.handleLogout, name='handleLogout'),

#   path('/admin', views.company_home, name='admin_home'),
]