from django.contrib import admin
from accounts.models import User, Student, EducationDetails
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(EducationDetails)
