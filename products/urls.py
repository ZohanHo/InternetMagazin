"""InternetMagazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ListViewLanding.as_view(), name = "landing"),
    path('auto/', ListViewLandingAuto.as_view(), name = "landingauto"),
    path('auto/add/', ListViewNewAuto.as_view(), name = "list_new_auto_url"),
    path('product/<pk>/', LandingDetailView.as_view(), name="product_detail_url"),
    path('add/', AddCarView.as_view(), name="create_car_url"),
    path('add/<pk>/', AddDetailView.as_view(), name="detail_new_car_url"),
    path('add/<pk>/update/', CarUpdateViwe.as_view(), name="update_car_url"),
    path('add/<pk>/delete/', CarDeleteView.as_view(), name="delete_car_url"),
]
