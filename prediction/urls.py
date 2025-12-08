# prediction/urls.py
from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    # Prediction URLs
    path('', views.prediction_home, name='prediction_home'),
    path('get_universities/', views.get_universities, name='get_universities'),
    path('get_majors_with_blocks/', views.get_majors_with_blocks, name='get_majors_with_blocks'),
    path('result/', views.prediction_result, name='prediction_result'),
    path('statistics/', views.statistics_dashboard, name='statistics_dashboard'),
    path('statistics/api/', views.statistics_api, name='statistics_api'),
]