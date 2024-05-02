from django.contrib import admin

from models_demo.vehicles.models import Dealership, RepairStation, VehicleOwner


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    pass


@admin.register(RepairStation)
class RepairStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'address',]
    list_filter = ['location',]


@admin.register(VehicleOwner)
class VehicleOwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number',]
    list_filter = ['first_name', 'last_name',]
    ordering = ['first_name', 'last_name',]

# Do the same for the rest if needed...
