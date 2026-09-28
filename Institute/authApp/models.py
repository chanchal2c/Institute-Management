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
  
  
class BasicInfo(models.Model):
  name = models.CharField(max_length=100, null=True)
  phone = models.CharField(max_length=15, null=True)
  email = models.EmailField(unique=True, null=True)
  address = models.TextField(null=True)
  date_of_birth = models.DateField(null=True)
  created_at = models.DateField(auto_now_add=True, null=True)
  updated_at = models.DateField(auto_now=True, null=True)
  
  def __str__(self):
    return f"{self.name}"