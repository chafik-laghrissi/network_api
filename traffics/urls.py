from django.urls import path
from .views import ListPoints, ListTraffics, DetailTraffic, DetailPoint, TrafficGroupedByPoint, TrafficStatistics, TrafficStatisticsPerPoint

urlpatterns = [
    path('traffic/<int:pk>/', DetailTraffic.as_view()),
    path('traffics/', ListTraffics.as_view()),
    path('point/<int:pk>/', DetailPoint.as_view()),
    path('points/', ListPoints.as_view()),
    path('traffics/by-point/<int:point_id>', TrafficGroupedByPoint.as_view()),
    path('traffics/statistics/', TrafficStatistics.as_view()),
    path('traffics/statistics/per-point', TrafficStatisticsPerPoint.as_view())
]
