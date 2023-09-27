from django.urls import path
from . import views 
urlpatterns = [
    path('ver_home/', views.ver_home, name="ver_home"),
    path('ver_home/adcionarItem/', views.adcionarItem, name="adcionarItem"),
    path('ver_home/adcionarItem/itemAdcionado/', views.itemAdcionado, name="itemAdcionado"),
    path('ver_home/remover_produto/<int:codigo>/', views.remover_produto, name='remover_produto'),
    path('ver_home/editarProduto/<int:codigo>/', views.editarProduto, name='editarProduto')
]