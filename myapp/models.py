from django.db import models

# Create your models here.


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/instructor_images')
    about = models.CharField(max_length=20)
    description = models.TextField()




class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/course_images')
    instructor  = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField()
    price = models.FloatField()
    hours = models.FloatField()


