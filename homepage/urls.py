from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat-history/', views.get_chat_history, name='get_chat_history'),
    path('<str:slug>', views.news_detail, name='news_detail')
]