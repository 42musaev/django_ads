from django.contrib import admin
from .models import Ads, District, DealType, HousingType, ProperType, \
    Finishing, Applications, Repair, Bathroom, Balcony, SunnySide, \
    ViewFromWindows, Door, ConnectedServices, Yard, Parking, Series, \
    YearConstruction, Walls, Elevator, HouseNumber, WindowMaterial


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone']
    list_display_links = ['user_name']


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


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Bathroom)
class BathroomAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Balcony)
class BalconyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(SunnySide)
class SunnySideAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(ViewFromWindows)
class ViewFromWindowsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(ConnectedServices)
class ConnectedServicesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Yard)
class YardAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(YearConstruction)
class YearConstructionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Walls)
class WallsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(HouseNumber)
class HouseNumberAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(WindowMaterial)
class WindowMaterialAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
