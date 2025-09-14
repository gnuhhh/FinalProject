from django.urls import path
from . import views
urlpatterns = [
    path('', views.college, name='college'),
    path('ha-noi', views.collegeHaNoi, name='collegeHaNoi'),
    path('tp-hcm', views.collegeTphcm, name='collegeTphcm'),
    path('college-<str:k>', views.collegedetail, name='collegedetail')
]