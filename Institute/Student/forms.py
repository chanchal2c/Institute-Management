from django import forms
from django.db import transaction
from .models import *
from authApp.models import CustomUser

class StudentForm(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = ['user']

    @transaction.atomic  
    def save(self, commit = True):
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='123456',
            user_type = 'Student'
        )
        student =  super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student