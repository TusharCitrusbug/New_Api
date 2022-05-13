from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    category_image=models.ImageField(default = "default.jpg", upload_to = "media")
    featured=models.BooleanField(default=True)
    def __str__(self):
        return self.category_name

class City(models.Model):
     city_name=models.CharField(max_length=100,unique=True)
     def __str__(self):
        return self.city_name
    
class Plan(models.Model):
    title=models.CharField(max_length=100,unique=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(null=True,blank=True)
    plan_datetime=models.DateTimeField(null=False,blank=False)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    postal_code=models.PositiveIntegerField(blank=False,null=False)
    plan_image=models.ImageField(default = "default.jpg", upload_to = "media")
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

class CSV_STORE(models.Model):
    csv_file=models.FileField(upload_to='media/')
    