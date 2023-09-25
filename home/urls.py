from django.urls import path
from . import views 
urlpatterns = [
    path('ver_home/', views.ver_home, name="ver_home"),
    path('ver_home/adcionarItem/', views.adcionarItem, name="adcionarItem"),
    path('ver_home/adcionarItem/itemAdcionado/', views.itemAdcionado, name="itemAdcionado")
]