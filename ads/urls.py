from django.urls import path

from .views import HomeView, FiltersAdsView, AddApplications, DetailAdsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filter/', FiltersAdsView.as_view(), name='filter'),
    path('add-applications/<str:pk>/', AddApplications.as_view(), name='add_applications'),
    path('ads/<int:pk>/', DetailAdsView.as_view(), name='ads_detail')
]
