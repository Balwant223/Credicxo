from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

def is_u_student(function=None,redirect_field_name=REDIRECT_FIELD_NAME):
    my_decorator=user_passes_test(
        lambda u:u.is_active and u.is_student,
        redirect_field_name=redirect_field_name)
    if function:
        return my_decorator(function)
    return my_decorator

def is_u_teacher(function=None,redirect_field_name=REDIRECT_FIELD_NAME):
    my_decorator=user_passes_test(
        lambda u:u.is_active and u.is_teacher,
        redirect_field_name=redirect_field_name)
    if function:
        return my_decorator(function)
    return my_decorator