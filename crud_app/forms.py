from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'auther', 'year_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group'}),
            'auther': forms.TextInput(attrs={'class': 'form-group'}),
            'year_published': forms.NumberInput(attrs={'class': 'form-group'}),
        }

    def clean_year_published(self):
        year = self.cleaned_data['year_published']
        if year < 0 or year > 9999:
            raise forms.ValidationError("Please enter a valid year (0-9999)")
        return year