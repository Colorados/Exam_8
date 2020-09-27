from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['']