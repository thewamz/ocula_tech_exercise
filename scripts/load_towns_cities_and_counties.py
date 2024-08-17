"""
Load towns, cities and counties from a csv file
"""
import csv

from django.db import transaction

from ocula.weatherapp.models import City, County


def run():
    with transaction.atomic():
        with open("scripts/towns_cities_counties.csv") as fhandle:
            csv_reader = csv.reader(fhandle, delimiter=",")

            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue

                city_name = row[0]
                county_name = row[1]

                county, _ = County.objects.get_or_create(name=county_name)

                _, _ = City.objects.get_or_create(name=city_name, county=county)
