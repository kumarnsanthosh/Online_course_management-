from .views import *
from django.urls import path

app_name = 'dashboard'

urlpatterns = [ path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
                path('all_courses/', all_courses, name='all_courses'),
                path('view_course/<int:id>/', view_course, name='view_course'),
                path('update_course/<int:id>/', update_course, name='admin_update_course'),
                path('delete_course/<int:id>/', delete_course, name='delete_course'),
                path('all_instructors/', all_instructors, name='all_instructors'),
                path('view_instructor/<int:id>/', view_instructor, name='view_instructor'),
                path('update_instructor/<int:id>/', update_instructor, name='update_instructor'),
                path('create_course/', create_course, name='create_course'),
                path('delete_instructor/<int:id>/', delete_instructor, name='admin_delete_instructor'),
                path('all_students/', all_students, name='all_students'),
                path('update_student/<int:id>/', update_student_profile, name='update_student'),
                path('delete_student/<int:id>/', delete_student, name='delete_student'),
                path('add_student/', register_student, name='add_student'),
                path('view_student/<int:id>/', student_profile, name='view_student'),
                 
            ]