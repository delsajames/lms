from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework import authentication
from accounts.serializers import UserSerializer,FacultySerializer
from accounts.permissions import IsFaculty
from accounts.models import Faculty


# Create your views here.

class UserCreateView(CreateAPIView):

    serializer_class=UserSerializer

class FacultyRetrieveUpdateView(RetrieveUpdateAPIView) :

    authentication_classes=[authentication.TokenAuthentication] 

    permission_classes=[IsFaculty]  

    serializer_class=FacultySerializer

    queryset=Faculty.objects.all()
    

