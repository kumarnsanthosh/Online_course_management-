from .views import *
from django.urls import path

app_name = 'myapp'

urlpatterns = [ path('', index, name='index'),
                path('course/<int:id>/', details, name='detail')
            ]