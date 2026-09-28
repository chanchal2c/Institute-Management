from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', teacher_list, name='teacher_list'),
]