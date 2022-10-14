from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('/signup/', views.handelSingup, name='handelSingup'),

  path('/login', views.handleLogin, name='handleLogin'),
  path('/logout', views.handleLogout, name='handleLogout'),
  
  path("/password_reset", views.password_reset_request, name="password_reset"),
  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      
#   path('/admin', views.company_home, name='admin_home'),
]