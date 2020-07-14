from django.urls import path

from .views import HomeView, FiltersAdsView, add_applications, DetailAdsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filter/', FiltersAdsView.as_view(), name='filter'),
    path('add-applications/', add_applications, name='add_applications'),
    path('ads/<int:pk>/', DetailAdsView.as_view(), name='ads_detail')
]
