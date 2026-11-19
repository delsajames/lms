from rest_framework import serializers
from accounts.models import User,Faculty,Student

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['id','username','password','email','phone','role']

        read_only_fields=['id']

def create(self,validated_data):

    return User.objects.create_user(**validated_data)

class FacultySerializer(serializers.ModelSerializer):

    class Meta:

        model=Faculty

        fields="__all__"


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model=Student

        fields="__all__"
