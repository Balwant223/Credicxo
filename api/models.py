from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def _create_user(self,email,password,**args):
        if not email:
            raise ValueError("User must have email")
        user= self.model(
            email=self.normalize_email(email),
            **args,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,password=None,**args):
        args.setdefault('is_staff',False)
        args.setdefault('is_superuser',False)
        return self._create_user(email, password, **args)
    def create_superuser(self,email,password,**args):
        args.setdefault('is_staff',True)
        args.setdefault('is_superuser',True)
        if args.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if args.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **args)

class MyUser(AbstractUser):
    is_student=models.BooleanField('student',default=True)
    is_teacher=models.BooleanField('teacher',default=False)
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=MyUserManager()

class Student(models.Model):
    classs=models.CharField(max_length=20)
    name=models.ForeignKey(MyUser, on_delete=models.CASCADE)