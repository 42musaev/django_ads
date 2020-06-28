from django.contrib import admin
from .models import Ads, District, DealType


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'deal_type', 'special_offer']
    list_editable = ['special_offer']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(DealType)
class DealTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
