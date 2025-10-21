from django.urls import path
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('hanoi/', views.school_hanoi, name='school_hanoi'),
    path('tphcm/', views.school_tphcm, name='school_tphcm'),
    path('<int:id>/', views.school_by_id, name='school_by_id'),
]