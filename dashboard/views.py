from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import InstructorForm
from user.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Activity
from myapp.forms import  CourseForm
from django.shortcuts import get_object_or_404
# Create your views here.



@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home') 
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
        'activities': Activity.objects.all().order_by('-created_at')[:5]


    }

    return render(request, 'admin_dashboard.html', context)

@login_required
def all_courses(request):
    if not request.user.is_superuser:
        return redirect('home') 
    course = Course.objects.all()
    return render(request, 'all_courses.html', {'course': course})

def creat_course(request):
    form = CourseForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Activity.objects.create(
                user=request.user.username,
                action=f"Course '{form.name}' created"
            )
            return redirect('dashboard:all_courses')
        else:
            print(form.errors)
    else:
        form = CourseForm()
    return render(request, 'admin_create_course.html', {'form':form})
    

@login_required
def view_course(request, id):
    if not request.user.is_superuser:
        return redirect('home')  
    course = Course.objects.get(id=id)
    return render(request, 'admin_course_detail.html', {'course': course})


@login_required
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Activity.objects.create(
                user=request.user,
                action=f"Course '{course.name}' updated"
            )
            return redirect('myapp:instructor')
    return render(request, 'admin_update_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('dashboard:all_courses')
    return render(request, 'admin_delete_course.html', {'course': course})


@login_required
def all_instructors(request):
    if not request.user.is_superuser:
        return redirect('home') 
    instructor = Instructor.objects.all()
    return render(request, 'all_instructors.html', {'instructors': instructor})

@login_required
def view_instructor(request, id):
    if not request.user.is_superuser:
        return redirect('home')  
    instructor = Instructor.objects.get(id=id)
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses
    }
    return render(request, 'admin_view_instructor.html', context)

@login_required
def update_instructor(request, id):
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST or None, request.FILES or None, instance=instructor)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard:all_instructors')
    
    else:
        form = InstructorForm()
    return render(request, 'admin_update_instructor.html', {'course': form})

@login_required
def delete_instructor(request, id):
    instructor = Instructor.objects.get(id=id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('dashboard:all_instructors')
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses
    }
    return render(request, 'admin_delete_instructor.html', context)


def admin_become_instructor(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        instructor, created = Instructor.objects.get_or_create(user=user)
        instructor.name = name
        instructor.description = description
        if image: 
            instructor.image = image
        instructor.save()
        return redirect('dashboard:all_courses')

    return render(request, 'become_instructor.html', {'user': user})