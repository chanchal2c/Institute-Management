from django import forms
from django.db import transaction
from .models import *


class TeacherForm(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = TeacherModel
        fields = '__all__'
        exclude = ['user']

    @transaction.atomic  
    def save(self, commit = True):
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='123456',
            user_type = 'teacher'
        )
        teacher =  super().save(commit=False)
        teacher.user = user
        if commit:
            teacher.save()
        return teacher
