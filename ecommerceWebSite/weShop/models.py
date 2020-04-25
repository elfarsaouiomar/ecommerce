from django.db import models
from django.db.models import Model


class Subscribe(Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
