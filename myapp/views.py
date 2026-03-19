from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    course  = Course.objects.all()[:4]
    return render(request, 'index.html',{'course': course})


def details(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'details.html', {'course': course}) 


def instructor_dashboard(request):
    instructor = request.user.instructor
    course = Course.objects.filter(instructor=instructor)
    return render(request, 'instructor.html', {'my_course':course})


def create_course(request):
    pass

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