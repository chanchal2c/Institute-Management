from django.db import models
from authApp.models import *

# Create your models here.

class StudentModel(BasicInfo):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    roll_no = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='media/student_images/', null=True)

    def __str__(self):
        return f"{self.name}"