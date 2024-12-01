from django.urls import path
from .views import SizePredictionView

urlpatterns = [
    path('predict-size/', SizePredictionView.as_view(), name='predict-size'),
]
