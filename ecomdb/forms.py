from django import forms
from django.forms.forms import Form
from .models import Product

class Product_form(forms.Form):
    name = forms.CharField(label='Name of product', max_length=50)
    price = forms.IntegerField(label='Price of product')
    quantity = forms.IntegerField(label='Quantity of product')

class Choose_form(forms.Form):
    id = forms.ModelChoiceField(queryset=Product.objects.values_list('id', flat=True))