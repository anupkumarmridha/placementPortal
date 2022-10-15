from django.urls import path
from accounts import views
from accounts import resetPasswordView
from accounts import studentView

urlpatterns = [
  path('/signup/', views.handelSingup, name='handelSingup'),
  path('activate/<uidb64>/<token>', views.activate, name='activate'),
  path('/login', views.handleLogin, name='handleLogin'),
  path('logout', views.handleLogout, name='handleLogout'),
  
  path('viewStudentProfile/',studentView.viewStudentProfile, name='viewStudentProfile'),

  # to reset password
  path('activate/<uidb64>/<token>', views.activate, name='activate'),
  
  path("password_change", resetPasswordView.password_change, name="password_change"),
  path("password_reset", resetPasswordView.password_reset_request, name="password_reset"),
  path('reset/<uidb64>/<token>', resetPasswordView.passwordResetConfirm, name='password_reset_confirm'),

  path('addStudentBasicProfileDetails/', studentView.addStudentBasicProfileDetails, name='addStudentBasicProfileDetails'),
  path('updateStudentBasicProfileDetails/',studentView.updateStudentBasicProfileDetails, name='StudentBasicProfileDetails'),
  path('addStudentEducationProfileDetails/', studentView.addStudentEducationProfileDetails, name='addStudentEducationProfileDetails'),
  path('updateStudentEducationProfileDetails/',studentView.updateStudentEducationProfileDetails, name='updateStudentEducationProfileDetails'),
  
#   path('/admin', views.company_home, name='admin_home'),
]