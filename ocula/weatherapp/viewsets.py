from datetime import datetime

from django.conf import settings

import requests
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from ocula.weatherapp.models import City, Temperature


class TemperatureSerializer(serializers.Serializer):
    minimum = serializers.FloatField()
    maximum = serializers.FloatField()
    average = serializers.FloatField()
    humidity = serializers.FloatField()


class TemperatureViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            city = City.objects.get(name__iexact=request.GET["city"])
        except City.DoesNotExist:
            return Response(
                {"message": "Invalid city! Please enter a valid UK city"}, status=404
            )

        try:
            temperature = Temperature.objects.get(
                city=city,
                recorded_at=datetime.strptime(request.GET["date"], "%Y-%m-%d"),
            )
        except Temperature.DoesNotExist:
            return Response(
                {"message": "No record found matching the city and date provided!"},
                status=404,
            )

        serializer = TemperatureSerializer(temperature)

        return Response(serializer.data)

    def create(self, request):
        try:
            city = City.objects.get(name__iexact=request.POST["city"])
        except City.DoesNotExist:
            return Response(
                {"message": "Invalid city! Please enter a valid UK city"}, status=404
            )

        recorded_at_date = datetime.strptime(request.POST["date"], "%Y-%m-%d")

        # retrieve city coordinates from Weather API
        if not any([city.longitude, city.latitude]):
            response = requests.get(
                "http://api.openweathermap.org/geo/1.0/direct?"
                f"q={city.name},GB&appid={settings.WEATHER_API_KEY}"
            )
            response_json = response.json()

            city.latitude = response_json[0]["lat"]
            city.longitude = response_json[0]["lon"]
            city.save()

        # retrieve temperate data from Weather API
        timestamp = int(recorded_at_date.timestamp())
        response = requests.get(
            "https://history.openweathermap.org/data/2.5/history/city?"
            f"lat={city.latitude}&lon={city.longitude}&type=hour&start={timestamp}&"
            f"end={timestamp}&appid={settings.WEATHER_API_KEY}"
        )
        response_json = response.json()

        temperature = Temperature.objects.create(
            minimum=response_json["list"][0]["main"]["temp_min"],
            maximum=response_json["list"][0]["main"]["temp_max"],
            average=response_json["list"][0]["main"]["temp"],
            humidity=response_json["list"][0]["main"]["humidity"],
            city=city,
            recorded_at=recorded_at_date,
        )
        serializer = TemperatureSerializer(temperature)

        return Response(serializer.data)
