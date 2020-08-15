from django.contrib import admin
from weShop.Models.models import Subscribe, Contact, Product, Category, Size, Service, Order, OrderItem, Country
from weShop.Models.translation import ProductTranslationOptions, CategoryTranslationOption

from modeltranslation.translator import register, translator



from oscar.apps.catalogue.models import Product, Category


translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOption)

#admin.site.register(Product)
#admin.site.register(Category)
admin.site.register(Size)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Country)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
      """
            this class used to change the view of the admin
      """
      list_display = ('name', 'description', 'icon')
      ordering = ('name',)
      search_fields = ('name', )


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
      """
            this class used to change the view of the admin
      """
      list_display = ('email','dateDeCreation')
      ordering = ('dateDeCreation',)
      search_fields = ('email', 'dateDeCreation', )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
      """
            this class used to change the view of the admin
      """
      list_display = ('firstname', 'lastname', 'email', 'subject', 'message', 'dateDeCreation')
      ordering = ('dateDeCreation',)
      search_fields = ('email', 'lastname', 'firstname', 'dateDeCreation')