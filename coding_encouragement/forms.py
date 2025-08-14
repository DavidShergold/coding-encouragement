from django import forms
from .models import Quote

class QuoteSubmissionForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Enter your motivational quote here...',
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Author name (optional)',
                'class': 'form-control'
            })
        }
        labels = {
            'text': 'Motivational Quote',
            'author': 'Author (Optional)'
        }
