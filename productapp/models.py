
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="category/",null=True,blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
            permissions = [
                ('admin_permisions', 'Admin Permission'),
                ('user_prmission', 'User Permission'),
            ]

class Product(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="product/",null=True,blank=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    created_date=models.DateField(default=timezone.now)
    updated_date=models.DateField(default=timezone.now)
    class Meta:
            permissions = [
                ('admin_permisions', 'Admin Permission'),
                ('user_prmission', 'User Permission'),
            ]

class Order(models.Model):
   user =models.ForeignKey(User, on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
   Quantity=models.IntegerField()
   status=models.CharField(max_length=15)
   price = models.DecimalField(max_digits=7, decimal_places=3)
   address=models.JSONField()
   created_date = models.DateTimeField(default=timezone.now)
   modify_date = models.DateTimeField(default=timezone.now)
