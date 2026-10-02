from django.shortcuts import render
from .forms import TeacherForm

# Create your views here.

def teacher_list(request):
  
    return render(request, 'teacher-list.html')


def teacher_add_view(request):

    form = TeacherForm()


    context = {
        'form': form,
        'form_title': 'Add Teacher Information',
        'form_btn': 'Add Teacher',
        'page_title': 'Add Teacher'
    }

    return render(request, 'master/base_form.html', context)