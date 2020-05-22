from django.contrib import admin
from .models import Subscribe, Contact, Product, Category, Size, Service, Order, OrderItem

admin.site.register(Subscribe)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)

