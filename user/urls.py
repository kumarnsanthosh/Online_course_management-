from .views import *
from django.urls import path

app_name = 'user'

urlpatterns = [ path('login/', loginpage, name='login'),
               path('logout/', logoutpage, name='logout'), 
                path('register/', register, name='register'),  

            ]