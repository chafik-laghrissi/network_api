from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Point, Traffic
from .serializers import PointSerializer, TrafficSerializer, TrafficSerializerSatistics,TrafficSerializerSatisticsPerPoint
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.


class ListPoints(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class ListTraffics(generics.ListCreateAPIView):
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer


class DetailTraffic(generics.RetrieveUpdateDestroyAPIView):
    queryset = Traffic.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TrafficSerializer


class DetailPoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class TrafficGroupedByPoint(generics.ListAPIView):
    queryset = Point.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TrafficSerializer

    def list(self, request: Request, point_id: int):
        queryset = Traffic.objects.raw(
            f'select * from traffics_traffic where point_id={point_id} order by day')
        serializer = TrafficSerializer(queryset, many=True)
        return Response(serializer.data)


class TrafficStatistics(generics.ListAPIView):
    queryset = Point.objects.raw(
        'select sum(point_id) as id, hour_interval ,sum(collective_transport) as collective_transport,sum(particular_transport) as particular_transport ,sum(haulage) as haulage from traffics_traffic group by hour_interval')
    serializer_class = TrafficSerializerSatistics
    permission_classes = (IsAuthorOrReadOnly,)


class TrafficStatisticsPerPoint(generics.ListAPIView):
    queryset = Point.objects.raw(
        'select point_id as id, sum(collective_transport) as collective_transport ,sum(particular_transport) as particular_transport,sum(haulage) as haulage, name as description from traffics_traffic join traffics_point on point_id=traffics_point.id group by point_id,name')
    serializer_class = TrafficSerializerSatisticsPerPoint
    permission_classes = (IsAuthorOrReadOnly,)
