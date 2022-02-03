from django.urls import path
from . import views

urlpatterns = [
    path('new', views.createSpider, name='spider-new'),
    path('<str:id>', views.details, name="spider-details"),
    path('<str:id>/update', views.updateSpider, name="spider-update"),
    path('<str:id>/delete', views.deleteSpider, name="spider-delete"),

    path('<str:id>/molts', views.molts, name="molts"),
    path('<str:id>/add-molt', views.createMolt, name="molt-create"),
    path('molts/<str:molt_id>/edit', views.updateMolt, name="molt-edit"),
    path('molts/<str:molt_id>/delete', views.deleteMolt, name="molt-delete"),
]
