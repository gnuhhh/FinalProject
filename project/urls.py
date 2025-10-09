"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("dj-admin/", admin.site.urls),
    path('', include('homepage.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('question/', include('question.urls')),
    path('advise/', include('advise.urls')),
    path('university/', include('university.urls')),
    path('college/', include('college.urls')),
    path('admin/', include('admin.urls')),
    path('profile/', include('user_profile.urls')),
    path('tests/', include('testapp.urls')),
    path('test-khoi/', include('testblock.urls')),
    path('du-doan-dai-hoc/', include('admission_predictor.urls')),
    path('compare/', include('daihoc_compare.urls')),
]
