from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type_data = ((1, "Admin"),(2, "Student"), (3, "PR"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=20)

