from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from terrakeeper.settings import MEDIA_ROOT


urlpatterns = [
    path('', include('spiders.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)