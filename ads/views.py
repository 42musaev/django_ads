from django.shortcuts import render
from django.views.generic.base import View

from .models import Ads


class HomeView(View):

    def get(self, request):
        ads = Ads.objects.filter(special_offer=True)
        return render(request, 'ads/index.html', {'ads': ads})
