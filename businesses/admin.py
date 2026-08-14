from django.contrib import admin

from .models import RentalBusiness


@admin.register(RentalBusiness)
class RentalBusinessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "location",
        "created_at",
    )

    search_fields = (
        "name",
        "location",
        "owner__username",
    )