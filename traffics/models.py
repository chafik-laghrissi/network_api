from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import Model, PointField
# Create your models here.


class Point (Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    location = PointField(srid=4326, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Traffic(models.Model):
    day = models.IntegerField()
    hour_interval = models.CharField(max_length=6)
    collective_transport = models.IntegerField(default=0)
    particular_transport = models.IntegerField(default=0)
    haulage = models.IntegerField(default=0)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=250, default='Traffic description')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)

    def __str__(self) -> str:
        return self.description
