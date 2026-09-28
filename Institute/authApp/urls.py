from django.urls import path
from .views import home_view, login_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('login/', login_view, name='login_view'),
]