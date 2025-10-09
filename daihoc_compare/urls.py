from django.urls import path
from . import views

app_name = 'daihoc_compare'  # ← QUAN TRỌNG: phải có dòng này

urlpatterns = [
    path('', views.compare_universities, name='compare_universities'),
    path('result/', views.compare_result, name='compare_result'),
]