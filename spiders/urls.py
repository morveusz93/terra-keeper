from django.urls import path
from spiders.views import ( MoltListView, PhotoDeleteView, SpiderDetailView, SpiderListView, SpiderDeleteView,
SpiderCreateView, SpiderUpdateView, MoltCreateView, MoltUpdateView, MoltDeleteView, HomePageView)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-profile',SpiderListView.as_view(), name='my-profile'),

    path('spiders/create', SpiderCreateView.as_view(), name='spider-create'),
    path('spiders/<str:pk>', SpiderDetailView.as_view(), name='spider-details'),
    path('spiders/<str:pk>/edit', SpiderUpdateView.as_view(), name='spider-update'),
    path('spiders/<str:pk>/delete', SpiderDeleteView.as_view(), name='spider-delete'),
    path('spiders/<str:pk>/delete-photo', PhotoDeleteView.as_view(), name='spider-delete-photo'),
    path('spiders/<str:pk>/molts', MoltListView.as_view(), name='spider-molts'),
    path('spiders/<str:pk>/addmolt', MoltCreateView.as_view(), name='molt-create'),
    path('spiders/molts/<str:pk>/edit', MoltUpdateView.as_view(), name='molt-edit'),
    path('spiders/molts/<str:pk>/delete', MoltDeleteView.as_view(), name='molt-delete'),
]
