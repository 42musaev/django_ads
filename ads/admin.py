from django.contrib import admin
from .models import Ads, District, DealType, HousingType, ProperType, Finishing


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'deal_type', 'special_offer']
    list_editable = ['special_offer']
    save_as = True


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(DealType)
class DealTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(HousingType)
class HousingTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(ProperType)
class ProperTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Finishing)
class FinishingAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
