from django.urls import path
from . import views

urlpatterns = [
    path('', views.spiders, name="spiders"),
    path('spiders/new', views.createSpider, name='spider-new'),
    path('spiders/<str:id>', views.details, name="spider-details"),
    path('spiders/<str:id>/update', views.updateSpider, name="spider-update"),
    path('spiders/<str:id>/delete', views.deleteSpider, name="spider-delete"),
    path('spiders/<str:id>/molts', views.showMolts, name="spider-molts"),
]
