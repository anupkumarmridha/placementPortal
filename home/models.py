from unittest.util import _MAX_LENGTH
from django.db import models
from accounts.models import User, Student
# Create your models here.

class Company(models.Model):
    companyName=models.CharField(max_length=255)
    #startup / MNC
    companyType=models.CharField(max_length=255)
    #hardware / software
    companyCategory=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.companyName


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    role = models.CharField(max_length = 255)
    description = models.TextField()
    ctc = models.DecimalField(max_digits = 10, decimal_places = 2)
    profile = models.CharField(max_length = 255)
    location = models.CharField(max_length = 500)
    
    open = models.BooleanField(default=False)
    pr = models.ForeignKey(Student, on_delete = models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #company requirement details

    def __str__(self):
        return self.role

class InterviewExperience(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    company=models.ForeignKey(Company, on_delete = models.CASCADE)
    jobProfile=models.CharField(max_length=500)
    experience=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ' | ' + str( self.company)
    
class Selection(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.student) + ' | ' + str( self.job)

class StudentJob(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    rounds = models.CharField(max_length=100)
    verdict_choice = (('Selected',"Selected"),('Under Review',"Under Review"), ('Rejected', "Rejected"), ('Selected For Next Round', "Selected For Next Round"))
    verdict = models.CharField(choices=verdict_choice, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.student) + ' | ' + str( self.rounds) + '|' + str(self.verdict)