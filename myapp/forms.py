from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'video', 'instructor', 'category', 'description',  'price', 'hours']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'address': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'bio': forms.Textarea(attrs={'class': 'w-full border p-2 rounded'}),
        } 