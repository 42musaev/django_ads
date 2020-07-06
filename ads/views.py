from django.views.generic import ListView
from .models import Ads, DealType, HousingType, ProperType, Finishing


class Filters:
    def get_deal_types(self):
        return DealType.objects.all()

    def get_housing_type(self):
        return HousingType.objects.all()

    def get_proper_type(self):
        return ProperType.objects.all()

    def get_finishing(self):
        return Finishing.objects.all()


class HomeView(Filters, ListView):
    model = Ads
    queryset = Ads.objects.filter(special_offer=True)
    context_object_name = 'ads'
    template_name = 'ads/index.html'


class SearchView(Filters, ListView):
    model = Ads
    queryset = Ads.objects.all()
    context_object_name = 'ads'


class FiltersAdsView(Filters, ListView):
    def get_queryset(self):
        queryset = Ads.objects.filter(
            deal_type__in=self.request.GET.getlist('deal_type'),
            housing_type__in=self.request.GET.getlist('housing_type'),
            proper_type__in=self.request.GET.getlist('proper_type'),
            finishing__in=self.request.GET.getlist('finishing'),
        )
        if not queryset.exists():
            queryset = Ads.objects.all()
        return queryset

    context_object_name = 'ads'
