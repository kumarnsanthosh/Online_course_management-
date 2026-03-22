from .views import *
from django.urls import path

app_name = 'myapp'

urlpatterns = [ path('', index, name='index'),
                path('course/<int:id>/', details, name='detail'),
                path('instructor/', instructor_dashboard, name='instructor'),
                path('create_course/', create_course, name='create_course')
            ]