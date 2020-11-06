from django.urls import path
from .views import CalculateSatOrSun

urlpatterns = [
    path('calculate/', CalculateSatOrSun.as_view()),
]
