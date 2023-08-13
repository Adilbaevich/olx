from django import forms
from .models import Product, Product1,Product2,Product3,Product4


class ProductForm(forms.ModelForm):
   class Meta:
    model = Product
    fields = 'title', 'image', 'description', 'price','author'

class Product3Form(forms.ModelForm):
   class Meta:
    model = Product3
    fields = 'title', 'image', 'description',  'price','author'
    
class Product2Form(forms.ModelForm):
   class Meta:
    model = Product2
    fields = 'title', 'image', 'description',  'price','author'
   
class Product4Form(forms.ModelForm):
   class Meta:
    model = Product4
    fields = 'title', 'image', 'description',  'price','author'