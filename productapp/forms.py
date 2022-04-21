from django.forms import ModelForm
from .models import Category,Product
from django import forms

class addCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields ='__all__'

class addProductForm(ModelForm):
    class Meta:
        model = Product
        fields =('name', 'image', 'price',
                  'category', )

class OrderForm(forms.Form):
    house_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'col-11 mb-3'}))
    Area=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'col-11 mb-3'}))
    pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'col-11 mb-3'}))
    city=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'col-11 mb-3'}))