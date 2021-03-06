from rest_framework import serializers
from .models import Traffic, Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class PointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Point
        geo_field = 'location'
        id_field = False
        fields = '__all__'


class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = "__all__"


class TrafficSerializerSatistics(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = ("hour_interval", "collective_transport","particular_transport","haulage")
class TrafficSerializerSatisticsPerPoint(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = ("id","description", "collective_transport","particular_transport","haulage")