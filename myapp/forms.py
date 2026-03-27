from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'video', 'category', 'description',  'price', 'hours']
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


