from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    course  = Course.objects.all()[:4]
    return render(request, 'index.html',{'course': course})


def details(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'details.html', {'course': course}) 


def instructor(request):
    return render(request, 'instructor.html')