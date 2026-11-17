from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES=(
        ("faculty","faculty"),
        ("student","student"),
    )

    phone=models.CharField(max_length=15)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

class Faculty(models.Model):

    qualification=models.CharField(max_length=200)    

    designation=models.CharField(max_length=200)

    experience=models.CharField(max_length=200)

    profile_picture=models.ImageField(null=True)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='faculties')


class Student(models.Model):

    dob=models.DateField(null=True)

    gender=models.CharField(max_length=100)

    college=models.CharField(max_length=200)

    qualification=models.CharField(max_length=200)

    profile_picture=models.ImageField(null=True)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='students')
