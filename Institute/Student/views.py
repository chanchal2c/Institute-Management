from django.shortcuts import render
from .views import *
from .models import *

# Create your views here.

def student_list(request):

    students = StudentModel.objects.all()

    context = {
        'students': students
    }
  
    return render(request, 'student-list.html', context)