from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', category_list_view, name='category_list_view'),
    path('category-add/', category_add_view, name='category_add_view'),
    path('category-edit/<int:category_id>/', category_edit_view, name='category_edit_view'),
    path('category-delete/<int:category_id>/', category_delete_view, name='category_delete_view'),
]