from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^shop-single/(?P<slug>[\w-]+)/$', views.singleProduct, name="singleProduct"),
    url(r'shop/q', views.findBy, name="getbyfilter"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'checkout/$', views.checkout, name="checkout"),
    url(r'thankyou/$', views.thankyou, name="thankyou"),
    url(r'contact/$', views.contact, name="contact"),
    url(r'^subscribe/$', views.subscribe, name="subscribe"),
]


