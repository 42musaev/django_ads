from django.urls import path

from .views import HomeView, SearchView, FiltersAdsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filter/', FiltersAdsView.as_view(), name='filter'),
]
