from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import InstructorForm
from user.form import ProfileForm, RegisterForm
from user.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Activity
from myapp.forms import  CourseForm
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@login_required
@staff_member_required
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
@staff_member_required
def all_courses(request):
    if not request.user.is_superuser:
        return redirect('home') 
    course = Course.objects.all()
    return render(request, 'all_courses.html', {'course': course})

@login_required
@staff_member_required
def create_course(request):
    if not hasattr(request.user, 'instructor'):
                Instructor.objects.create(user=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES or None)
        if form.is_valid():
            course = form.save(commit=False)
            if not hasattr(request.user, 'instructor'):
                Instructor.objects.create(user=request.user)
            course.instructor = request.user.instructor
            course.save()
            Activity.objects.create(
                user=request.user,
                action=f"Course '{course.name}' created"
            )
            return redirect('dashboard:all_courses')
        else:
            print("Form errors:", form.errors)
    else:
        form = CourseForm()
    return render(request, 'admin_create_course.html', {'form': form})


    
@login_required
@staff_member_required
def view_course(request, id):
    if not request.user.is_superuser:
        return redirect('home')  
    course = Course.objects.get(id=id)
    return render(request, 'admin_course_detail.html', {'course': course})


@staff_member_required
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
@staff_member_required
def delete_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('dashboard:all_courses')
    return render(request, 'admin_delete_course.html', {'course': course})


@login_required
@staff_member_required
def all_instructors(request):
    if not request.user.is_superuser:
        return redirect('home') 
    instructor = Instructor.objects.all()
    return render(request, 'all_instructors.html', {'instructors': instructor})

@login_required
@staff_member_required
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
@staff_member_required
def update_instructor(request, id):
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST or None, request.FILES or None, instance=instructor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard:all_instructors')
    return render(request, 'admin_update_instructor.html', {'form': form, 'instructor': instructor})

@login_required
@staff_member_required
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

@login_required
@staff_member_required
def profile(request):
    pro, created =  Student.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile':pro})

@login_required
@staff_member_required
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
    
    return render(request, 'editprofile.html', {'form': form})

@login_required
@staff_member_required
def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html',{'students':students})

@login_required
@staff_member_required
def student_profile(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student_profile.html',{'student':student})

@login_required
@staff_member_required
def update_student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            Activity.objects.create(
                user=request.user,
                action=f"User '{request.user.username}' updated profile"
            )
            return redirect('dashboard:all_students')
        else:
            form.errors
    else:
        form = ProfileForm(instance=student)
    return render(request, 'edit_student_profile.html', {'form': form, 'profile': student})

@login_required
@staff_member_required
def register_student(request):
    form = RegisterForm(request.POST or None)
    user = request.POST.get('username')
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            Student.objects.get_or_create(user=user)
            Activity.objects.create( user=user,action=f"User '{user.username}' registered")
            return redirect('dashboard:all_students')
    return render(request, 'student_register.html',  {'form':form})

@login_required
@staff_member_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        user = student.user
        student.delete()
        user.delete()
        return redirect('dashboard:all_students')

    return render(request, 'admin_delete_student.html', {'student': student})

