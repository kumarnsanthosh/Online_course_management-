from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from myapp.views import index
from .form import RegisterForm, ProfileForm
from .models import Student
from dashboard.models import Activity
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
    user = request.POST.get('username') or request.user
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            Activity.objects.create( user=user, 
                                    action=f"User '{user.username}' registered")
            return redirect('user:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html',  {'form':form})


def profile(request):
    pro, created =  Student.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile':pro})


def update_profile(request):
    student, created = Student.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            Activity.objects.create(
                user=request.user,
                action=f"User '{request.user.username}' updated profile"
            )
            return redirect('user:profile')
        else:
            form.errors
    else:
        form = ProfileForm(instance=student)
    
    return render(request, 'editprofile.html', {'form': form, 'profile': student})