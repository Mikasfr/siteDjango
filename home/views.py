from django.shortcuts import render
from django.http import HttpResponse

def ver_home(request):
    return render(request, 'home.html')


def inserir_produtos(request):
    return HttpResponse('estou no inserir')