from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='static/images/instructor_images', default='static/images/profile-pic.png')
    description =  models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name or 'instructor'
    


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
        
    name =  models.CharField(max_length=100)
    image =  models.ImageField(upload_to='static/images/course_images',null=True, blank=True)
    video =  models.FileField(upload_to='static/video_upload', null=True, blank=True, validators= [FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    instructor =  models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category =  models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    description =  models.TextField()
    rating =  models.FloatField(null=True, blank=True)
    price =  models.FloatField()
    hours =  models.FloatField()




