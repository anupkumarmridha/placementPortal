from django.contrib import admin
from home.models import Company, Job, InterviewExperience, Selection, StudentJob
# Register your models here.
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(InterviewExperience)
admin.site.register(Selection)
admin.site.register(StudentJob)

