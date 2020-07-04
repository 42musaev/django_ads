from django.urls import path

from .views import HomeView, search

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
]
