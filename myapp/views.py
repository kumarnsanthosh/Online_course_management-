from django.shortcuts import render, redirect
from .models import *
from .forms import  CourseForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    course  = Course.objects.all()[:4]
    return render(request, 'index.html',{'course': course})


def details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'details.html', {'course': course}) 


def instructor_dashboard(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('create_course')
    instructor = request.user.instructor
    course = Course.objects.filter(instructor=instructor)
    return render(request, 'instructor.html', {'my_course':course, 'instructor':instructor})


def create_course(request):
    form = CourseForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            course = form.save(commit=False)
            if not hasattr(request.user, 'instructor'):
                Instructor.objects.create(user=request.user)
            course.instructor = request.user.instructor
            course.save()
            return redirect('myapp:instructor')
        else:
            print(form.errors)
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form':form})


def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    # 🔒 Security: only owner can edit
    if not course.instructor.user or course.instructor.user != request.user:
        return redirect('myapp:instructor')
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:instructor')
        else:
            print(form.errors)
    return render(request, 'update_course.html', {'form': form, 'course': course})

def view_course(request):
    pass

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)

    # 🔒 Security: only owner can delete
    if not hasattr(request.user, 'instructor') or course.instructor.user != request.user:
        return redirect('myapp:instructor')

    if request.method == 'POST':
        course.delete()
        return redirect('myapp:instructor')

    return render(request, 'delete_course.html', {'course': course})


def become_instructor(request):
    if hasattr(request.user, 'instructor'):
        return redirect('myapp:instructor')

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Instructor.objects.create(
            user=request.user,
            name=name,
            description=description,
            image=image
        )

        return redirect('myapp:instructor')

    return render(request, 'become_instructor.html')

def update_instructor(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('become_instructor')

    instructor = request.user.instructor

    if request.method == 'POST':
        instructor.name = request.POST.get('name')
        instructor.description = request.POST.get('description')

        if request.FILES.get('image'):
            instructor.image = request.FILES.get('image')

        instructor.save()
        return redirect('myapp:instructor')

    return render(request, 'update_instructor.html', {'instructor': instructor})



def delete_instructor(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('myapp:instructor')

    instructor = request.user.instructor

    if request.method == 'POST':
        instructor.delete()
        return redirect('home')  # or wherever

    return render(request, 'delete_instructor.html', {'instructor': instructor})


def create_student(request):
    pass

def update_student(request):
    pass

def view_student(request):
    pass

def delete_student(request):
    pass