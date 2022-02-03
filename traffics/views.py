from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Point, Traffic
from .serializers import PointSerializer, TrafficSerializer
# Create your views here.


class ListPoints(generics.ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class ListTraffics(generics.ListAPIView):
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer


class DetailTraffic(generics.RetrieveUpdateDestroyAPIView):
    queryset = Traffic.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TrafficSerializer


class DetailPoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Traffic.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PointSerializer
