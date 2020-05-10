from django.db import models
from django.db.models import Model
from datetime import datetime, date


class Subscribe(Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email


class Contact(Model):
    fname = models.CharField(max_length=30, blank=False, null=True)
    lname = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.fname


class Size(Model):
    size = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.size

class Service(Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    icon = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Category(Model):
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='categorys/', default='upload/categorys/children.jpg')

    def __str__(self):
        return self.name


class Product(Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=True)
    summary = models.TextField(max_length=100, blank=False, null=True)
    description = models.TextField(max_length=3000)
    price = models.FloatField(max_length=10)
    quantity = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    isNew = models.BooleanField(default=True)
    inStock = models.BooleanField(default=True)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='upload/', default=None)
    dateDeCreation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

