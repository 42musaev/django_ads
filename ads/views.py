from django.shortcuts import render
from django.views.generic.base import View

from .models import Ads


class HomeView(View):
    def get(self, request):
        ads = Ads.objects.filter(special_offer=True)
        return render(request, 'ads/index.html', {
            'ads': ads,
        })


def search(request):
    if request.GET:
        deal_type = request.GET['deal_type']
        housing_type = request.GET['housing_type']
        proper_type = request.GET['proper_type']
        finishing = request.GET['finishing']
        ads = Ads.objects.filter(
            deal_type__name=deal_type,
            housing_type__name=housing_type,
            proper_type__name=proper_type,
            finishing__name=finishing,
        )
    ads = Ads.objects.all()
    return render(request, 'ads/search-page.html', {'ads': ads})
