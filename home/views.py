from django.shortcuts import render
from django.http import HttpResponse

# criando as funções e ligando com as urls onde serão executadas

def ver_home(request):
    return render(request, 'home.html')
# linkando o html

def inserir_produtos(request):
    return HttpResponse('estou no inserir')