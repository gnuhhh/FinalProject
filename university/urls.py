from django.urls import path
from . import views
urlpatterns = [
    path('', views.university, name='university'),
    path('ha-noi', views.universityHaNoi, name='universityHaNoi'),
    path('tp-hcm', views.universityTphcm, name='universityTphcm'),
    path('university-<str:k>', views.unidetail, name='unidetail')
]