from django.db import models

# Create your models here.
class Job(models.Model):
    role = models.CharField(max_length = 255)
    description = models.TextField()
    ctc = models.CharField(max_length = 10)
    profile = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    location = models.CharField(max_length = 500)
