from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def teacher_list(request):
  
    return render(request, 'teacher-list.html')


def teacher_add_view(request):

    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher added successfully.')
            return redirect('teacher_list')


    context = {
        'form': form,
        'form_title': 'Add Teacher Information',
        'form_btn': 'Add Teacher',
        'page_title': 'Add Teacher'
    }

    return render(request, 'master/base_form.html', context)