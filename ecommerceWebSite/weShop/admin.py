from django.contrib import admin
from weShop.Models.models import Subscribe, Contact, Product, Category, Size, Service, Order, OrderItem, Country

admin.site.register(Subscribe)
#admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Country)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
      list_display = ('firstname', 'lastname', 'email', 'subject', 'message', 'dateDeCreation')
      ordering = ('dateDeCreation',)
      search_fields = ('email', 'lastname', 'firstname', 'dateDeCreation')