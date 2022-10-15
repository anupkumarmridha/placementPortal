from django.db import models

from accounts.models import Student

# Create your models here.
class Job(models.Model):
    description = models.TextField()
    ctc = models.CharField(max_length = 10)
    profile = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    location = models.CharField(max_length = 500)
    open = models.BooleanField(default=False)
    pr = models.OneToOneField(Student, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Selection(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE)
    job = models.OneToOneField(Job, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
