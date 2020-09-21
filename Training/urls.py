from django.contrib import admin
from django.urls import path
from . import views

app_name="training"
urlpatterns = [
    path('main/', views.Home_Page,name="main_page"),
    path('test/', views.Test,name="test"),
    path('analysis/', views.pie_chart,name="analysis"),
    path('', views.Test ,name="main")
]
