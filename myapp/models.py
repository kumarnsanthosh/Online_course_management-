from django.db import models

# Create your models here.


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static/images/instructor_images')
    description = models.TextField()
    def __str__(self):
        return self.name



class Course(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/course_images')
    video = models.CharField(max_length=500, default='video-link')
    instructor  = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField()
    price = models.FloatField()
    hours = models.FloatField()


