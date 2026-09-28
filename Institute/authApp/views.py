from django.shortcuts import redirect, render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')
  
  
def login_view(request):
  
    form = AuthenticationForm()
    
    if request.method == 'POST':
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home_view')

    context = {
        'form': form
    }  
    
    return render(request, 'login.html', context)