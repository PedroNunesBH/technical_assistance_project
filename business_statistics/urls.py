from django.urls import path
from .views import TechnicalsStatisticsView

urlpatterns = [
    path("technicals_statistics/", TechnicalsStatisticsView.as_view(), name="technicals_statistics"),
]
