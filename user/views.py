from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from myapp.views import index
from .form import RegisterForm
# Create your views here.


def loginpage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username, password=password)
    if user:
        login(request, user)
        return redirect('myapp:index')
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('user:login')

def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'register.html',  {'form':form})