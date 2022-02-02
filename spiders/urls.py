from django.urls import path
from . import views

urlpatterns = [
    path('', views.spiders, name="spiders"),
    path('spiders/new', views.createSpider, name='spider-new'),
    path('spiders/<str:id>', views.details, name="spider-details"),
    path('spiders/<str:id>/update', views.updateSpider, name="spider-update"),
    path('spiders/<str:id>/delete', views.deleteSpider, name="spider-delete"),

    path('spiders/<str:id>/molts', views.molts, name="molts"),
    path('spiders/<str:id>/add-molt', views.createMolt, name="molt-create"),
    path('spiders/molts/<str:molt_id>/edit', views.updateMolt, name="molt-edit"),
    path('spiders/molts/<str:molt_id>/delete', views.deleteMolt, name="molt-delete"),
]
