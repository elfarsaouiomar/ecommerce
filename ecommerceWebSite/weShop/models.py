from django.db import models
from django.db.models import Model, AutoField, EmailField,\
    CharField, TextField, ImageField, BooleanField, DateField,\
    IntegerField, FloatField, ForeignKey, PROTECT, ManyToManyField
from datetime import datetime, date
from django.conf import settings


class Subscribe(Model):
    id = AutoField(primary_key=True)
    email = EmailField(max_length=254)

    def __str__(self):
        return self.email

class Contact(Model):
    fname = CharField(max_length=30, blank=False, null=True)
    lname = CharField(max_length=30, blank=False, null=True)
    email = EmailField(max_length=100)
    subject = CharField(max_length=50)
    message = TextField(max_length=300)

    def __str__(self):
        return self.fname

class Size(Model):
    size = CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.size

class Service(Model):
    name = CharField(max_length=100)
    description = TextField(max_length=300)
    icon = CharField(max_length=40)

    def __str__(self):
        return self.name

class Category(Model):
    name = CharField(max_length=100, primary_key=True)
    image = ImageField(upload_to='categorys/', default='upload/categorys/children.jpg')

    def __str__(self):
        return self.name

class Product(Model):

    id = AutoField(primary_key=True)
    name = CharField(max_length=40, blank=False, null=True)
    summary = TextField(max_length=100, blank=False, null=True)
    description = TextField(max_length=3000)
    price = FloatField(max_length=10)
    quantity = IntegerField()
    size = ForeignKey(Size, on_delete=PROTECT)
    category = ForeignKey(Category, on_delete=PROTECT)
    isNew = BooleanField(default=True)
    inStock = BooleanField(default=True)
    isActive = BooleanField(default=True)
    rank = IntegerField(default=1)
    image = ImageField(upload_to='upload/', default=None)
    dateDeCreation = DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrderItem(Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    dateDeCreation = DateField(auto_now_add=True)

    def __str__(self):
        return "new Order by  {0}".format(self.user)

    def get_total_item_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    """
        ref_code = models.CharField(max_length=20, blank=True, null=True)
        start_date = models.DateTimeField(auto_now_add=True)
        ordered_date = models.DateTimeField()
        ordered = models.BooleanField(default=False)
        being_delivered = models.BooleanField(default=False)
        received = models.BooleanField(default=False)
        refund_requested = models.BooleanField(default=False)
        refund_granted = models.BooleanField(default=False)
    """
