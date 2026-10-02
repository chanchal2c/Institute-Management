from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

def category_list_view(request):

    categories = CategoryModel.objects.all()

    context = {
        'categories': categories
    }
    
    return render(request, 'category_list.html', context)


def category_add_view(request):

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('category_list_view')


    context = {
        'form': form,
        'form_title': 'Add Category Information',
        'form_btn': 'Add Category',
        'page_title': 'Add Category'
    }

    return render(request, 'master/base_form.html', context)



def category_edit_view(request, category_id):

    each_category = CategoryModel.objects.get(id=category_id)

    form = CategoryForm(instance=each_category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=each_category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('category_list_view')


    context = {
        'form': form,
        'form_title': 'Edit Category Information',
        'form_btn': 'Update Category',
        'page_title': 'Edit Category'
    }

    return render(request, 'master/base_form.html', context)


def category_delete_view(request, category_id):

    each_category = CategoryModel.objects.get(id=category_id)
    each_category.delete()
    messages.success(request, 'Category deleted successfully.')
    
    return redirect('category_list_view')


# ---------Course Views-----------------

def course_list_view(request):

    courses = CourseModel.objects.all()

    context = {
        'courses': courses
    }
    
    return render(request, 'course_list.html', context)


def course_add_view(request):

    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully.')
            return redirect('course_list_view')


    context = {
        'form': form,
        'form_title': 'Add Course Information',
        'form_btn': 'Add Course',
        'page_title': 'Add Course'
    }

    return render(request, 'master/base_form.html', context)



def course_edit_view(request, course_id):

    each_course = CourseModel.objects.get(id=course_id)

    form = CourseForm(instance=each_course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=each_course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('course_list_view')


    context = {
        'form': form,
        'form_title': 'Edit Course Information',
        'form_btn': 'Update Course',
        'page_title': 'Edit Course'
    }

    return render(request, 'master/base_form.html', context)



def course_delete_view(request, course_id):

    each_course = CourseModel.objects.get(id=course_id)
    each_course.delete()
    messages.success(request, 'Course deleted successfully.')

    return redirect('course_list_view')