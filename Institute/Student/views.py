from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def student_list(request):

    students = StudentModel.objects.all()

    context = {
        'students': students
    }
  
    return render(request, 'student-list.html', context)


def student_add_view(request):

    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')


    context = {
        'form': form,
        'form_title': 'Add Student Information',
        'form_btn': 'Add Student',
        'page_title': 'Add Student'
    }

    return render(request, 'master/base_form.html', context)