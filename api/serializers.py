from rest_framework import serializers
from .models import MyUser,Student

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('first_name','email')
        model=MyUser
class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('classs','name')
        model=Student