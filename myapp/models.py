from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description =  models.TextField()
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Course(models.Model):
    def __str__(self):
        return self.name

    name        =  models.CharField(max_length=100)
    image       =  models.ImageField(upload_to='static/images/course_images')
    video       =  models.FileField(upload_to='static/video_upload', null=True, validators= [FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    instructor  =  models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category    =  models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    description =  models.TextField()
    rating      =  models.FloatField()
    price       =  models.FloatField()
    hours       =  models.FloatField()




