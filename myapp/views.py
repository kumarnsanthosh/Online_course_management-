from django.shortcuts import render, redirect
from .models import *
from .forms import  CourseForm
# Create your views here.


def index(request):
    course  = Course.objects.all()[:4]
    return render(request, 'index.html',{'course': course})


def details(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'details.html', {'course': course}) 


def instructor_dashboard(request):
    if not hasattr(request.user, 'instructor'):
        instructor = Instructor.objects.create(user=request.user)
    instructor = request.user.instructor
    course = Course.objects.filter(instructor=instructor)
    return render(request, 'instructor.html', {'my_course':course})


def create_course(request):
    form = CourseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(instructor_dashboard)
    else:
        form = CourseForm()
        return render(request, 'create_course.html', {'form':form})

def update_course(request):
    pass

def view_course(request):
    pass

def delete_course(request):
    pass


def create_instructor(request):
    pass

def update_instructor(request):
    pass

def view_instructor(request):
    pass

def delete_instructor(request):
    pass


def create_student(request):
    pass

def update_student(request):
    pass

def view_student(request):
    pass

def delete_student(request):
    pass