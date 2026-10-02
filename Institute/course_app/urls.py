from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', category_list_view, name='category_list_view'),
]