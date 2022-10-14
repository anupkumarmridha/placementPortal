from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type_data = ((1, "Admin"),(2, "Student"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=20)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    roll=models.CharField(max_length=9, unique=True)
    dept= models.CharField(max_length=255)
    course= models.CharField(max_length=255)
    graduationYear=models.DateField()
    cgpa= models.DecimalField(max_digits=2, decimal_places=2)
    resume= models.FileField(null=True, blank=True, upload_to='PDF/Students/resume/')
    isPR=models.BooleanField(default=False)

    gender_choice=(('M',"Male"),('F',"Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/Students/profile/')
    phone = models.CharField(max_length=13)
    dob = models.DateField()
    
    homeAddress = models.TextField()
    localAddress = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

