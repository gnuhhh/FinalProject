from django.urls import path
from .views import login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout')
]