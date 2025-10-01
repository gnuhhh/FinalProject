from django.urls import path
from .views import index, available_dates, available_slots, payment

urlpatterns = [
    path('', index, name='advise'),
    path('payment', payment, name='payment'),
    path('available-dates/', available_dates, name='advise_available_dates'),
    path('available-slots/', available_slots, name='advise_available_slots'),
]