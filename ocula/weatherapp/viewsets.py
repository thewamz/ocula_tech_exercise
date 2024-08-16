from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ocula.weatherapp.models import Temperature, City

from datetime import datetime


class TemperatureSerializer(serializers.Serializer):
    minimum = serializers.FloatField()
    maximum = serializers.FloatField()
    average = serializers.FloatField()
    humidity = serializers.FloatField()


class TemperatureViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            city = City.objects.get(name__iexact=request.GET['city'])
        except City.DoesNotExist:
            return Response({'message': 'Invalid city! Please enter a valid UK city'}, status=404)

        try:
            temperature = Temperature.objects.get(city=city, recorded_at=datetime.strptime(request.GET['date'], '%Y-%m-%d'))
        except Temperature.DoesNotExist:
            return Response({'message': 'No record found matching the city and date provided!'}, status=404)

        serializer = TemperatureSerializer(temperature)

        return Response(serializer.data)

    def create(self, request):
        pass