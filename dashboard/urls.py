from .views import *
from django.urls import path

app_name = 'dashboard'

urlpatterns = [ path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
                path('all_courses/', all_courses, name='all_courses'),
                path('view_course/<int:id>/', view_course, name='view_course'),
                path('all_instructors/', all_instructors, name='all_instructors'),
                path('view_instructor/<int:id>/', view_instructor, name='view_instructor'),
                path('update_instructor/<int:id>/', update_instructor, name='update_instructor'),
                path('delete_instructor/<int:id>/', delete_instructor, name='delete_instructor'),
            #    path('add_courses/', add_instructor, name='add_instructor'),
            #    path('update_student/<int:id>/', update_student, name='update_student'),
            #    path('delete_student/<int:id>', delete_student, name='delete_student'),
            #    path('add_student/', add_student, name='add_student'),
                 
            ]