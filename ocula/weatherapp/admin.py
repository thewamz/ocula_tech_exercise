from django.contrib import admin

from ocula.weatherapp.models import (
    BuyerQuestion,
    BuyerRequest,
    County,
    EstateAgentResponse,
    Outcode,
    PropertyFeature,
    PropertyType,
    ResidentialProperty,
    ResidentialPropertyImage,
    TownCity,
    UserDetail,
)


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "firstname",
        "lastname",
    )
    raw_id_fields = ("user",)
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    def firstname(self, obj):
        return obj.user.first_name

    def lastname(self, obj):
        return obj.user.last_name


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PropertyFeature)
class PropertyFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ml_label",
    )


@admin.register(BuyerRequest)
class BuyerRequestAdmin(admin.ModelAdmin):
    list_display = (
        "view_towns_cities",
        "bedrooms",
        "max_price",
        "reason_to_buy",
        "user",
    )
    raw_id_fields = ("user",)
    list_filter = (
        "bedrooms",
        "reason_to_buy",
    )

    def view_towns_cities(self, obj):
        return ", ".join(town_city.name for town_city in obj.towns_cities.all())


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TownCity)
class TownCityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "county",
    )
    raw_id_fields = ("county",)
    search_fields = (
        "name",
        "county__name",
    )


@admin.register(Outcode)
class OutcodeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ResidentialProperty)
class ResidentialPropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "bedrooms",
        "property_type",
        "bathrooms",
        "town_city",
        "town_city_str",
        "price",
        "estate_agent_branch",
    )
    raw_id_fields = (
        "estate_agent_branch",
        "town_city",
        "property_type",
    )
    search_fields = (
        "town_city__name",
        "property_type__name",
        "estate_agent_branch__estate_agent__name",
    )
    list_filter = (
        "bedrooms",
        "bathrooms",
        "property_type",
        "town_city",
    )


@admin.register(ResidentialPropertyImage)
class ResidentialPropertyImageAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "residential_property",
    )
    raw_id_fields = ("residential_property",)


@admin.register(BuyerQuestion)
class BuyerQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "residential_property",
    )
    raw_id_fields = (
        "user",
        "residential_property",
    )
    search_fields = ("user__username",)


@admin.register(EstateAgentResponse)
class EstateAgentResponseAdmin(admin.ModelAdmin):
    list_display = ("buyer_question",)
    raw_id_fields = ("buyer_question",)
