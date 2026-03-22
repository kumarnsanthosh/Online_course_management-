from django import forms
from .models import Course


class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = '__all__'