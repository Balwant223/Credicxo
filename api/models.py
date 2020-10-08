from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def _create_user(self,username,password,**args):
        if not username:
            raise ValueError("User must have username")
        user= self.model(
            username=self.username
            **args,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,username,password=None,**args):
        args.setdefault('is_staff',False)
        args.setdefault('is_superuser',False)
        return self._create_user(username, password, **args)
    def create_superuser(self,username,password,**args):
        args.setdefault('is_staff',True)
        args.setdefault('is_superuser',True)
        if args.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if args.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **args)

class MyUser(AbstractUser):
    unique_id=models.IntegerField(unique=True)
    is_student=models.BooleanField('student',default=True)
    is_teacher=models.BooleanField('teacher',default=False)
    objects=MyUserManager()

class Student(models.Model):
    classs=models.CharField(max_length=20)
    name=models.ForeignKey(MyUser, on_delete=models.CASCADE)