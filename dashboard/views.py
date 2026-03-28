from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import InstructorForm
from user.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.



@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    avg_rating = Course.objects.aggregate(avg=Avg('rating'))['avg']
    overall_platform_quality = round(avg_rating,1)
    top_courses = Course.objects.order_by('-rating')[:12] 
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_instructors': Instructor.objects.count(),
        'overall_platform_quality':overall_platform_quality,
        'total_revenue' : sum(course.sell_price for course in Course.objects.all()),
        'top_courses' : top_courses,

    }

    return render(request, 'admin_dashboard.html', context)

@login_required
def all_courses(request):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    course = Course.objects.all()
    return render(request, 'all_courses.html', {'course': course})

@login_required
def view_course(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    course = Course.objects.get(id=id)
    return render(request, 'admin_detail.html', {'course': course})


@login_required
def update_course(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    course = Course.objects.get(id=id)
    return render(request, 'admin_update_course.html', {'course': course})

@login_required
def delete_course(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    course = Course.objects.get(id=id)
    return render(request, 'delete_course.html', {'course': course})


@login_required
def all_instructors(request):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    instructor = Instructor.objects.all()
    return render(request, 'all_instructors.html', {'instructors': instructor})

@login_required
def view_instructor(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    instructor = Instructor.objects.get(id=id)
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses
    }
    return render(request, 'view_instructor.html', context)

@login_required
def update_instructor(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST or None, request.FILES or None, instance=instructor)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard:view_instructor', id=instructor.id)
        else:
            print(form.errors)  # For debugging
    
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses,
        'form': form
    }
    return render(request, 'update_instructor.html', context)

@login_required
def delete_instructor(request, id):
    if not request.user.is_superuser:
        return redirect('home')  # restrict access
    instructor = Instructor.objects.get(id=id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('dashboard:all_instructors')
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses
    }
    return render(request, 'delete_instructor.html', context)

