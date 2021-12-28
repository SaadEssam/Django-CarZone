from django.shortcuts import redirect, render

# Create your views here.


def login(request):
  return render(request, 'accounts/login.html')

def register(request):
  if request.method == 'POST':
    print('method done')
    return redirect('register')
  
  else:
    return render(request, 'accounts/register.html')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')

def logout(request):
  return redirect('home')