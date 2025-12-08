from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_info, name='user_profile'), 
    path('cancel_appointment/<int:id>/', views.cancel_appointment, name='cancel_appointment'),
]