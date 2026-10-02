from django.shortcuts import render
from .models import *

# Create your views here.

def category_list_view(request):

    categories = CategoryModel.objects.all()

    context = {
        'categories': categories
    }
    
    return render(request, 'category_list.html', context)