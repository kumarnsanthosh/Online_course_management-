from django.db import models

# Create your models here.


class Instructor(models.Model):
    name        =  models.CharField(max_length=30)
    image       =  models.ImageField(upload_to='static/images/instructor_images')
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
    video       =  models.CharField(max_length=1000, default='video-link')
    instructor  =  models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category    =  models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    description =  models.TextField()
    rating      =  models.FloatField()
    price       =  models.FloatField()
    hours       =  models.FloatField()




