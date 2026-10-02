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


def student_add_view(request):


    context = {
        'form_title': 'Add Student Information',
        'form_btn': 'Add Student',
        'page_title': 'Add Student'
    }

    return render(request, 'master/base_form.html', context)