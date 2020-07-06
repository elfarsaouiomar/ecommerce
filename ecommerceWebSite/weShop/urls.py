from django.conf.urls import url
from .Controllers import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^shop-single/(?P<slug>[\d-]+)/$', views.singleProduct, name="singleProduct"),
    url(r'catigory/(?P<slug>[\w-]+)', views.categorys, name="catigory"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^addToCart/$', views.addOrUpdate, name='addOrUpdate'),
    url(r'deleteFromCart/(?P<slug>[\w-]+)', views.deleteFromCart, name='deleteFromCart'),
    url(r'checkout/$', views.checkout, name="checkout"),
    url(r'thankyou/$', views.thankyou, name="thankyou"),
    url(r'contact/$', views.contact, name="contact"),
    url(r'^subscribe/$', views.subscribe, name="subscribe"),



    url(r'^api/',views.api, name="api"),
    url(r'^api/id/(?P<slug>[\d-]+)/$',views.apibyId, name="apiById")
    #site.com/apibyid/slug
]


