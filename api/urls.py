from django.urls import path
from .views import SizePredictionView, ModelMetricsView

urlpatterns = [
    path('predict-size/', SizePredictionView.as_view(), name='predict-size'),
    path('model-metrics/', ModelMetricsView.as_view(), name='model-metrics'),
]
