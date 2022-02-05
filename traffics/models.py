from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import Model, PointField
from django.contrib.gis.geos import Point as PT
# Create your models here.


class Point (Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    location = PointField(srid=4326, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True,
                                 verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True,
                                  verbose_name='Longitude')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.location = PT(self.longitude, self.latitude)
        super().save(*args, **kwargs)
    


class Traffic(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    hour_interval = models.CharField(max_length=6)
    day = models.IntegerField()
    collective_transport = models.IntegerField(default=0)
    particular_transport = models.IntegerField(default=0)
    haulage = models.IntegerField(default=0)
    description = models.CharField(
        max_length=250, default='Traffic description',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.description
