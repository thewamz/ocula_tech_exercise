from django.urls import include, path

from rest_framework import routers

from .viewsets import TemperatureViewSet

app_name = "weatherapp"

router_v1 = routers.DefaultRouter()
router_v1.register(r"temperature", TemperatureViewSet, basename="temperature")

urlpatterns = [
    path("api/v1/", include(router_v1.urls)),
]
