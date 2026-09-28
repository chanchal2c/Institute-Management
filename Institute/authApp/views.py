from django.shortcuts import redirect, render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'home.html')
  
  
def login_view(request):
  
    form = AuthenticationForm()
    
    if request.method == 'POST':
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Successfully logged in!")
        return redirect('home_view')

    context = {
        'form': form
    }  
    
    return render(request, 'login.html', context)
  
  
def logout_view(request):
  
    logout(request)
    messages.success(request, "Successfully logged out!")
    
    return redirect('login_view')