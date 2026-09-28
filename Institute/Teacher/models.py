from django.db import models
from authApp.models import *

# Create your models here.

class TeacherModel(BasicInfo):
    subject = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/teacher_images/', null=True)

    def __str__(self):
        return f"{self.name}"