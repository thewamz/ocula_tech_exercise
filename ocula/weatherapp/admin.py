from django.contrib import admin

from ocula.weatherapp.models import City, County, Temperature


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "county",
    )
    raw_id_fields = ("county",)
    search_fields = (
        "name",
        "county__name",
    )


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = (
        "minimum",
        "maximum",
        "average",
        "humidity",
        "city",
        "recorded_at",
    )
    raw_id_fields = ("city",)
    search_fields = (
        "name",
        "city__name",
    )
