from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):
  return render(request, 'accounts/login.html')

def register(request):
  if request.method == 'POST':
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    
    if password == confirm_password:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exists!')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Email already exists!')
          return redirect('register')
        else:
          user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
          auth.login(request, user)
          messages.success(request, 'You are now logged in.')
          user.save()
          return redirect('dashboard')
          # messages.success(request, 'You are registered successfully.')
          # retrun redirect('login')
          
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')
    
  else:
    return render(request, 'accounts/register.html')


def dashboard(request):
  return render(request, 'accounts/dashboard.html')

def logout(request):
  return redirect('home')