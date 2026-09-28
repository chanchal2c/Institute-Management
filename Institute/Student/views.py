from django.shortcuts import render
from .views import *

# Create your views here.

def student_list(request):
  
    return render(request, 'student-list.html')