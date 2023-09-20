from django.shortcuts import render
from django.http import HttpResponse

# criando as funções e ligando com as urls onde serão executadas

def ver_home(request):
    return render(request, 'home.html')
# linkando o html

def adcionarItem(request):
    return render(request, 'adcionarItem.html')
#     if request.method == "get":
#         return render(request, 'adcionarItem.html')
#     # elif request.method ==  "post":
#     #     return

def itemAdcionado(request):
    return render(request, 'itemAdcionado.html')