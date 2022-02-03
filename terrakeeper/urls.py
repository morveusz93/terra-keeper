from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('spiders/', include('spiders.urls')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
