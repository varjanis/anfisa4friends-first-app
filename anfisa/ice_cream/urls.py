
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком мороженого
    path('ice_cream/', views.ice_cream_list),
    # Страница с информацией об одном сорте мороженого;
    # в качестве параметра ожидает целое положительное число или 0
    path('ice_cream/<int:pk>/', views.ice_cream_detail),
] 