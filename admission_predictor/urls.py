from django.urls import path
from . import views

app_name = 'admission_predictor'

urlpatterns = [
    path('du-doan-dai-hoc/', views.predict_admission, name='predict_admission'),
    path('ket-qua-du-doan/', views.predict_admission_result, name='predict_admission_result'),
]