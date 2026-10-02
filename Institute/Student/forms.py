from django import forms
from .models import *

class StudentForm(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = ['user']