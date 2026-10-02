from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"