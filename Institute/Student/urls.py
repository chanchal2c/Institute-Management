from django.urls import path
from .views import *

urlpatterns = [
    path('student_list/', student_list, name='student_list'),
    path('student_add/', student_add_view, name='student_add_view'),
]