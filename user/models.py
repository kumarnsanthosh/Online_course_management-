from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_pic =  models.ImageField(upload_to='static/images/profile_pictures', default='/static/images/user-image.png')
    bio = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    
    