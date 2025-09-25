from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.loginadmin, name='admin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('information', views.information, name='information'),
    path('information/create', views.information_create, name='information_create'),
    path('information/update/<str:id>', views.information_update, name='information_update'),
    path('information/delete/<str:id>', views.information_delete, name='information_delete'),
    path('news', views.news, name='news'),
    path('news/create', views.news_create, name='news_create'),
    path('news/update/<str:id>', views.news_update, name='news_update'),
    path('news/delete/<str:id>', views.news_delete, name='news_delete'),
    path('accounts', views.accounts, name='accounts'),
    path('accounts/create', views.accounts_create, name='accounts_create'),
    path('accounts/delete/<str:id>', views.accounts_delete, name='accounts_delete'),
    path('schedule', views.schedule, name='schedule'),
    path('expert', views.expert_view, name='expert'),
    path('expert/create', views.expert_create, name='expert_create'),
    path('expert/update/<str:id>', views.expert_update, name='expert_update'),
    path('expert/delete/<str:id>', views.expert_delete, name='expert_delete'),
    path('logout/', LogoutView.as_view(next_page='index'), name = 'logout_admin'),
]