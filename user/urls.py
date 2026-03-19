from .views import *
from django.urls import path

app_name = 'user'

urlpatterns = [ path('login/', loginpage, name='login'),
                path('logout/', logoutpage, name='logout'), 
                path('register/', register, name='register'),
                path('profile/', profile, name='profile'),
                path('update_profile/', update_profile, name='edit_profile')    

            ]