from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_pic =  models.ImageField(upload_to='images/profile_pictures/')
    bio = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
    
    
    