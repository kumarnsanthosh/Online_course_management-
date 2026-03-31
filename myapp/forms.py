from django import forms
from .models import Course, Instructor


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'video', 'category', 'description', 'instructor', 'price', 'hours']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border p-2 rounded'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border p-2 rounded'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border p-2 rounded'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border p-2 rounded'
            }),
            'hours': forms.NumberInput(attrs={
                'class': 'w-full border p-2 rounded'
            }),
        }


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border p-2 rounded',
                'placeholder': 'Enter instructor name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border p-2 rounded',
                'placeholder': 'Enter instructor bio or description',
                'rows': 5
            }),
            'image': forms.FileInput(attrs={
                'class': 'hidden',
                'accept': 'image/*'
            }),
        }


