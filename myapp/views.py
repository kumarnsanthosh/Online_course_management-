from django.shortcuts import render, redirect
from .models import *
from .forms import  CourseForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.models import Activity

# Create your views here.


@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('myapp:index')
    
    
    return render(request, 'admin_panel.html')

def index(request):
    trending_course  = Course.objects.all()[:4]
    subcategories = SubCategory.objects.prefetch_related('course_set')[:4]
    category = Category.objects.all()
    return render(request, 'index.html',{'course': trending_course , 'subcategories':subcategories, 'category':category})


def details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'details.html', {'course': course}) 


def instructor_dashboard(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('myapp:index')
    instructor = request.user.instructor
    course = Course.objects.filter(instructor=instructor)
    return render(request, 'instructor.html', {'my_course':course, 'instructor':instructor})


def create_course(request):
    form = CourseForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user.instructor
            course.save()
            Activity.objects.create(
                user=request.user,
                action=f"Course '{course.name}' created"
            )
            return redirect('myapp:instructor')
        else:
            print(form.errors)
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form':form})


def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if not course.instructor.user or course.instructor.user != request.user:
        return redirect('myapp:instructor')
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Activity.objects.create(
                user=request.user,
                action=f"Course '{course.name}' updated"
            )
            return redirect('myapp:instructor')
    return render(request, 'update_course.html', {'form': form, 'course': course})

def view_course(request):
    pass

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)

    if not hasattr(request.user, 'instructor') or course.instructor.user != request.user:
        return redirect('myapp:instructor')

    if request.method == 'POST':
        name = course.name
        course.delete()
        Activity.objects.create(
        user=request.user,
        action=f"Course '{name}' deleted"
    )
        return redirect('myapp:instructor')

    return render(request, 'delete_course.html', {'course': course})


def become_instructor(request):
    user = request.user
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

    return render(request, 'become_instructor.html', {'user':user})

def update_instructor(request, id):


    instructor = request.user.instructor

    if request.method == 'POST':
        instructor.name = request.POST.get('name')
        instructor.description = request.POST.get('description')

        if request.FILES.get('image'):
            instructor.image = request.FILES.get('image')

        instructor.save()
        return redirect('myapp:instructor')

    return render(request, 'update_instructor.html', {'instructor': instructor})



def delete_instructor(request, id):
    if not hasattr(request.user, 'instructor'):
        return redirect('myapp:instructor')

    user = request.user
    instructor = Instructor.objects.get(user=user)
    courses = instructor.courses.all()
    print(courses)
    if request.method == 'POST':
        instructor.delete()
        return redirect('myapp:index') 

    return render(request, 'delete_instructor.html', {'instructor': instructor})


def search(request):
    input_text = request.GET.get('search', '')
    print(input_text)
    text = Course.objects.filter(name__contains=input_text)
    return render(request, 'search_result.html', {'text':text, 'input_text':input_text})


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('course')
    total_price = sum(item.course.sell_price for item in cart_items)
    total_original_price = sum(item.course.price for item in cart_items)
    total_savings = total_original_price - total_price
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_original_price': total_original_price,
        'total_savings': total_savings,
    }
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, course=course)
    Activity.objects.create(
        user=request.user,
        action=f"Added '{course.name}' to cart"
    )
    return redirect('myapp:view_cart')


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    course_name = cart_item.course.name
    cart_item.delete()
    Activity.objects.create(
        user=request.user,
        action=f"Removed '{course_name}' from cart"
    )
    return redirect('myapp:view_cart')


def course_catogory(request, name):
    category = Category.objects.get(name=name)
    subcategories = SubCategory.objects.filter(main_category=category)
    return render(request, 'courses.html', {'category': category, 'subcategories': subcategories})

