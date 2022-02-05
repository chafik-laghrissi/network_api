from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Point, Traffic
from .serializers import PointSerializer, TrafficSerializer
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

    def list(self, request: Request,point_id:int):
        queryset = Traffic.objects.raw(f'select * from traffics_traffic where point_id={point_id} order by day')
        serializer = TrafficSerializer(queryset, many=True)
        return Response(serializer.data)
