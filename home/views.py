from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos
from django import db
from django.shortcuts import redirect
from .forms import ProdutoForm

# criando as funções e ligando com as urls onde serão executadas

def ver_home(request):
    produtos = Produtos.objects.all()
    return render(request, 'home.html', {'produtos' : produtos})
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

def remover_produto(request, codigo):
    try:
        # Use o código do produto para encontrar o objeto do produto no banco de dados
        produto = Produtos.objects.get(codigo=codigo)
        
        # Realize a remoção do produto
        produto.delete()

        # Redirecione de volta para a página de estoque após a remoção
        return redirect('ver_home')

    except Produtos.DoesNotExist:
        # Lidar com o caso em que o produto não existe
        # Você pode retornar uma página de erro ou uma mensagem apropriada aqui
        pass

def editarProduto(request, codigo):
    try:
        # Use o código do produto para encontrar o objeto do produto no banco de dados
        produto = Produtos.objects.get(codigo=codigo)
        if request.method == 'POST':
            # Se o formulário for enviado, atualize os dados do produto com base nos dados do formulário
            form = ProdutoForm(request.POST, instance=produto)
            if form.is_valid():
                form.save()
                # Redirecione de volta para a página de estoque após a edição
                return redirect('ver_home')
        else:
            # Se o formulário não foi enviado, crie um formulário pré-preenchido com os dados do produto
            form = ProdutoForm(instance=produto)

        return render(request, 'editarProduto.html', {'form': form, 'produtos': Produtos})

    except Produtos.DoesNotExist:
        # Lidar com o caso em que o produto não existe
        # Você pode retornar uma página de erro ou uma mensagem apropriada aqui
        pass
