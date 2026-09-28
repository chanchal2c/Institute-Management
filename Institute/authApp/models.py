from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
  USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('teacher', 'Teacher')
  )
  
  user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
  
  def str__(self):
    return f"{self.username} ({self.user_type})"