from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail
# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES=(
        ("faculty","faculty"),
        ("student","student"),
    )

    phone=models.CharField(max_length=15,unique=True)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

class Faculty(models.Model):

    qualification=models.CharField(max_length=200,null=True)    

    designation=models.CharField(max_length=200,null=True)

    experience=models.CharField(max_length=200,null=True)

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='faculties')

class Student(models.Model):

    age=models.PositiveIntegerField(null=True)

    gender=models.CharField(max_length=100,null=True)

    college=models.CharField(max_length=200,null=True)

    profile_picture=models.ImageField(upload_to="profile_picture",null=True)

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='students')


def create_faculty_profile(sender,instance,created,**kwargs):

    if created and instance.role=="faculty":

        Faculty.objects.create(owner=instance)

post_save.connect(create_faculty_profile,sender=User)

def create_student_profile(sender,instance,created,**kwargs):

    if created and instance.roles=="student":

        Student.objects.create(owner=instance)

post_save.connect(create_student_profile,sender=User)      

def send_email_notification(sender,instance,created,**kwargs):

    if created:

        send_mail(

               subject="account invitation",
               from_email="delsajames@gmail.com",
               recipient_list=["jancyag349@gmail.com"],
               message="your account is created")

post_save.connect(send_email_notification,sender=User)                
        
