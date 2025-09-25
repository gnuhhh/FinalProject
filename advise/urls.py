from django.urls import path
from .views import index, available_dates, available_slots

urlpatterns = [
    path('', index, name='advise'),
    path('available-dates/', available_dates, name='advise_available_dates'),
    path('available-slots/', available_slots, name='advise_available_slots'),
]