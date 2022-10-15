from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type_data = ((1, "Admin"),(2, "Student"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default=2, choices=user_type_data, max_length=20)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone=models.CharField(max_length=13, blank=True, null=True)
    personalEmail= models.CharField(max_length=255, blank=True, null=True)
    gender_choice=(('M',"Male"),('F',"Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/Students/profile/')
    dob = models.DateField()
    
    isSelected = models.BooleanField(default=False)
    
    homeAddress = models.TextField()
    localAddress = models.TextField()
    job_choice=(('Intern',"Internship"),('Placements',"Placements"))
    jobType = models.CharField(choices=job_choice, max_length=20)

    isPR=models.BooleanField(default=False)

    fatherName=models.CharField(max_length=255, blank=True, null=True)
    motherName=models.CharField(max_length=255, blank=True, null=True)
    guardianPhone=models.CharField(max_length=13, blank=True, null=True)  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

class EducationDetails(models.Model):

    student= models.ForeignKey(Student, on_delete = models.CASCADE)
    roll=models.CharField(max_length=9, unique=True)
    
    degreeLevelChoice=(('UG',"UG"),('PG',"PG"))
    degreeLevel= models.CharField(choices=degreeLevelChoice, max_length=20)
    currentDept= models.CharField(max_length=255)
    currentCourse= models.CharField(max_length=255)
    currentCgpa= models.DecimalField(max_digits=5, decimal_places=2)
    currentCourseGraduationYear=models.DateField(blank=True, null=True)

    class10Percentage=models.DecimalField(max_digits=5, decimal_places=2)
    class12Percentage=models.DecimalField(max_digits=5, decimal_places=2)
    
    ugDegree=models.CharField(max_length=255, blank=True, null=True)
    ugCgpa=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ugCollage=models.CharField(max_length=5, blank=True, null=True)
    ugGraduationYear=models.DateField(blank=True, null=True)
    resume= models.FileField(null=True, blank=True, upload_to='PDF/Students/resume/')
    def __str__(self):
        return str(self.user)