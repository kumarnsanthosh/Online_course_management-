from .views import *
from django.urls import path

app_name = 'myapp'

urlpatterns = [ path('', index, name='index'),
                path('course/<int:id>/', details, name='detail'),
                path('instructor/', instructor_dashboard, name='instructor'),
                path('create_course/', create_course, name='create_course'),
                path('update_course/<int:id>/', update_course, name='update_course'),
                path('delete_course/<int:id>/', delete_course, name='delete_course'),
                path('become-instructor/', become_instructor, name='become_instructor'),
                path('update_instructor/', update_instructor, name='update_instructor'),
                path('delete_instructor/', delete_instructor, name='delete_instructor'),
            ]