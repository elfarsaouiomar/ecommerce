from django.conf.urls import url, include
from django.contrib import admin
from django.apps import apps
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('weShop.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^oscar/', include(apps.get_app_config('oscar').urls[0])),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)