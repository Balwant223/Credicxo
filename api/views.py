from rest_framework import viewsets
from .models import MyUser,Student
from .serializers import UserListSerializer,StudentDetailSerializer
from rest_framework.exceptions import PermissionDenied
from common.decorators import is_u_student,is_u_teacher,is_u_su
from django.utils.decorators import method_decorator

class AllUser(viewsets.ModelViewSet):
    serializer_class=UserListSerializer
    @method_decorator(is_u_su())
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return MyUser.objects.all()
        raise PermissionDenied()
    @method_decorator(is_u_teacher())
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return MyUser.objects.filter(is_student=True)
    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)
class StudentList(viewsets.ModelViewSet):
    serializer_class=StudentDetailSerializer
    @method_decorator(is_u_student())
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return Student.objects.get(name=user)