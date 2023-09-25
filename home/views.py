from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos
from django import db

# criando as funções e ligando com as urls onde serão executadas

def ver_home(request):
    return render(request, 'home.html')
# linkando o html

def adcionarItem(request):
    if request.method == "GET":
         return render(request, 'adcionarItem.html')
    elif request.method == "POST":
        quantidade = request.POST.get('quantidade')
        codigo = request.POST.get('codigo')
        descricao = request.POST.get('descricao')
        aplicacao = request.POST.get('aplicacao')
        valor = request.POST.get('valor')
        produtos = Produtos(quantidade=quantidade, codigo=codigo, descricao=descricao, aplicacao=aplicacao, valor=valor )
        produtos.save()
        return render(request, 'itemAdcionado.html')

def itemAdcionado(request):
    return render(request, 'itemAdcionado.html')