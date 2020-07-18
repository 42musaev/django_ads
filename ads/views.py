from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Ads, DealType, HousingType, ProperType, Finishing
from .forms import ApplicationsForm


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = ApplicationsForm()
        return context


class AdsList(Filters, ListView):
    model = Ads
    queryset = Ads.objects.filter(special_offer=True)
    context_object_name = 'ads'
    template_name = 'ads_list.html'
    paginate_by = 8


class FiltersAdsView(Filters, ListView):
    def get_queryset(self):
        queryset = Ads.objects.filter(
            deal_type__in=self.request.GET.getlist('deal_type'),
            housing_type__in=self.request.GET.getlist('housing_type'),
            proper_type__in=self.request.GET.getlist('proper_type'),
            finishing__in=self.request.GET.getlist('finishing'),
        )

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["deal_type"] = ''.join(
            [f"deal_type={x}&" for x in self.request.GET.getlist("deal_type")]
        )
        context["housing_type"] = ''.join(
            [f"housing_type={x}&" for x in
             self.request.GET.getlist("housing_type")]
        )
        context["proper_type"] = ''.join(
            [f"proper_type={x}&" for x in
             self.request.GET.getlist("proper_type")]
        )
        context["finishing"] = ''.join(
            [f"finishing={x}&" for x in self.request.GET.getlist("finishing")]
        )

        return context

    paginate_by = 8
    context_object_name = 'ads'


class DetailAdsView(DetailView):
    model = Ads
    context_object_name = 'ads'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = ApplicationsForm()
        id = str(kwargs.get('object'))
        context['success_detail'] = f"success_detail{id.lstrip('ID: ')}"
        return context


class AddApplications(View):
    def post(self, request, pk):
        form = ApplicationsForm(request.POST)
        if form.is_valid():
            if not pk == 'None':
                form = form.save(commit=False)
                ads = Ads.objects.get(pk=int(pk))
                form.ads = ads
                request.session.set_expiry(28800)
                request.session[f'success_detail{int(pk)}'] = True
                form.save()
                return redirect(ads)
            request.session.set_expiry(28800)
            request.session['success_index'] = True
            form.save()
        return redirect('/#add_applications')
