
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class County(BaseModel):
    class Meta(BaseModel.Meta):
        verbose_name_plural = "counties"

    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    class Meta(BaseModel.Meta):
        verbose_name_plural = "cities"
        unique_together = ["name", "county"]

    name = models.CharField(max_length=300)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="cities")
    latitude = models.CharField(null=True, blank=True)
    longitude = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name


class Temperature(BaseModel):
    minimum = models.FloatField()
    maximum = models.FloatField()
    average = models.FloatField()
    humidity = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities")
    recorded_at = models.DateField()

    def __str__(self):
        return str(self.pk)
