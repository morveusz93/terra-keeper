from django.urls import path
from spiders.views import ( MoltListView, SpiderDetailView, SpiderListView, SpiderDeleteView,
SpiderCreateView, SpiderUpdateView, MoltCreateView, MoltUpdateView, MoltDeleteView, HomePageView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-profile', login_required(SpiderListView.as_view()), name='my-profile'),

    path('spiders/create', login_required(SpiderCreateView.as_view()), name='spider-create'),
    path('spiders/<str:pk>', login_required(SpiderDetailView.as_view()), name='spider-details'),
    path('spiders/<str:pk>/edit', login_required(SpiderUpdateView.as_view()), name='spider-update'),
    path('spiders/<str:pk>/delete>', login_required(SpiderDeleteView.as_view()), name='spider-delete'),
    path('spiders/<str:pk>/molts', login_required(MoltListView.as_view()), name='spider-molts'),
    path('spiders/<str:pk>/addmolt', login_required(MoltCreateView.as_view()), name='molt-create'),
    path('spiders/molts/<str:pk>/edit', login_required(MoltUpdateView.as_view()), name='molt-edit'),
    path('spiders/molts/<str:pk>/delete', login_required(MoltDeleteView.as_view()), name='molt-delete'),
]
