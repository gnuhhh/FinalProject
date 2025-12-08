from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>', views.chat_view, name='chat_view'),
]