from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),

                  path('', include('apps.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT) + static(
    STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
