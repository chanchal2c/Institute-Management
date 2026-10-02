from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/add/', teacher_add_view, name='teacher_add_view'),
]