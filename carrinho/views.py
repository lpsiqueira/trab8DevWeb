from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .carrinho import Carrinho
from .forms import RemoveItem
from appsite.models import Projeto

# Create your views here.
def carrinhoTeste(request):
    return HttpResponse('Ola')

def carrinho(request):
    carrinho = Carrinho(request)

    if request.method == 'POST':
        form = RemoveItem(request.POST, auto_id=False)
        form.is_valid()

        if request.POST.get('remover') == 'true':
            carrinho.remover(request.POST.get('id'))
            return HttpResponse()

        else:
            quantidade = int(request.POST.get('quantidade'))
            if quantidade != '':
                idQuantidade = request.POST.get('id')
                carrinho.alterar(idQuantidade, quantidade)
                quantidade = carrinho.getCarrinho()[idQuantidade]['quantidade']
                saida = {'quantidade': quantidade}
                return JsonResponse(saida)

    else:
        form = RemoveItem(auto_id=False)

    itens = []
    context = {'form': form}

    itensCarrinho = carrinho.getCarrinho()
    for item in itensCarrinho:
        proj = Projeto.objects.get(pk=itensCarrinho[item]['id'])
        itens.append({'nome': proj.nomeProjeto, 'qtd': itensCarrinho[item]['quantidade'], 'id': itensCarrinho[item]['id']})        
    context['itens'] = itens

    return render(request, 'carrinho/carrinho.html', context)


def adiciona(request, idProjeto):
    carrinho = Carrinho(request)
    
    carrinho.adicionar(idProjeto)
    response = 'carrinho alterado'
    
    return redirect('appsite:busca')