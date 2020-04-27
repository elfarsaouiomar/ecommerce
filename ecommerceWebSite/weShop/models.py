from django.db import models
from django.db.models import Model


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
