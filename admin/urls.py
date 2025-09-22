from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.loginadmin, name='admin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/information', views.information, name='information'),
    path('dashboard/information/create', views.information_create, name='information_create'),
    path('dashboard/information/update/<str:id>', views.information_update, name='information_update'),
    path('dashboard/information/delete/<str:id>', views.information_delete, name='information_delete'),
    path('dashboard/news', views.news, name='news'),
    path('dashboard/news/create', views.news_create, name='news_create'),
    path('dashboard/news/update/<str:id>', views.news_update, name='news_update'),
    path('dashboard/news/delete/<str:id>', views.news_delete, name='news_delete'),
    path('dashboard/accounts', views.accounts, name='accounts'),
    path('dashboard/accounts/create', views.accounts_create, name='accounts_create'),
    path('dashboard/accounts/delete/<str:id>', views.accounts_delete, name='accounts_delete'),
    path('dashboard/schedule', views.schedule, name='schedule'),
    path('logout/', LogoutView.as_view(next_page='index'), name = 'logout_admin'),
]