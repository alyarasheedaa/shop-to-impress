from django.forms import ModelForm
from main.models import MoodEntry
from django import forms

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["product", "description", "price", "image_url"]


        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL here'}),  # URL input
        }
