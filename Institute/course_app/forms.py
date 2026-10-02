from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name', 'description']


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = ['name', 'description', 'category', 'credit']