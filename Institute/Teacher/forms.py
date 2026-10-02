from django import forms
from .models import *


class TeacherForm(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = TeacherModel
        fields = '__all__'
        exclude = ['user']