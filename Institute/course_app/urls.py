from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', category_list_view, name='category_list_view'),
    path('category-add/', category_add_view, name='category_add_view'),
    path('category-edit/<int:category_id>/', category_edit_view, name='category_edit_view'),
    path('category-delete/<int:category_id>/', category_delete_view, name='category_delete_view'),

    # --------Course urls-----------------
    path('course-list/', course_list_view, name='course_list_view'),
    path('course-add/', course_add_view, name='course_add_view'),
    path('course-edit/<int:course_id>/', course_edit_view, name='course_edit_view'),
    path('course-delete/<int:course_id>/', course_delete_view, name='course_delete_view'),
]