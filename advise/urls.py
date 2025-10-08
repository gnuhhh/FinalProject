from django.urls import path
from .views import index, available_dates, available_slots, payment, expert_schedule, payment_return, payment_ipn

urlpatterns = [
    path('', index, name='advise'),
    path('payment', payment, name='payment'),
    path('payment/vnpay_return/', payment_return, name='payment_return'),
    path('payment/vnpay_ipn/', payment_ipn, name='payment_ipn'),
    path('available-dates/', available_dates, name='advise_available_dates'),
    path('available-slots/', available_slots, name='advise_available_slots'),
    path('expert-schedule/', expert_schedule, name='advise_expert_schedule'),
    
]