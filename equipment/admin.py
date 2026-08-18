from django.contrib import admin
from .models import Equipment,EquipmentUnit

@admin.register(Equipment)

class EquipmentAdmin(admin.ModelAdmin):
    list_display=("name","category","business","rental_price","deposit")

    search_fields=("name","category","business__name")


@admin.register(EquipmentUnit)

class EquipmentUnitAdmin(admin.ModelAdmin):
    list_display=("serial_number","equipment","status","condition")

    list_filter=("status","condition")

    search_fields=("equipment__name","serial_number")