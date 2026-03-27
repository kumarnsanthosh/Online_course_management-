from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image   = models.ImageField(upload_to='instructor_images/')
    description =  models.TextField(blank=True, null=True)
    def __str__(self):
        if self.user:
            return self.user.username
        return self.name or "Instructor"
    


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
    image =  models.ImageField(upload_to='course_images/',null=True, blank=True)
    video =  models.FileField(upload_to='video_upload/', null=True, blank=True, validators= [FileExtensionValidator(allowed_extensions=['mov','avi','mp4','webm','mkv'])])
    instructor =  models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    category =  models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    description =  models.TextField()
    rating =  models.FloatField(default=4)
    price =  models.FloatField()
    discount = models.FloatField(default=86.67)
    hours =  models.FloatField()

    @property
    def discount_amount(self):
        return round((self.price * self.discount)/100)
    
    @property
    def sell_price(self):
        return round(self.price - self.discount_amount)




