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
        if form.is_valid():
            if form.cleaned_data['remover']:
                #i = Carrinho.objects.get(pk=form.cleaned_data['item_id'])                
                #i.delete()
                carrinho.remover(form.cleaned_data['item_id'])
                print(form.cleaned_data['remover'])
        else:
            quantidade = request.POST.get('quantidade')
            if quantidade != '':
                idQuantidade = request.POST.get('id')
                #itemQtd = Carrinho.objects.get(pk=idQuantidade)                
                #itemQtd.quantidade = quantidade
                #itemQtd.save()
                carrinho.alterar(idQuantidade, quantidade)
                #itemQtd = Carrinho.objects.get(pk=idQuantidade)
                #quantidade = itemQtd.quantidade
                quantidade = carrinho.getCarrinho()[idQuantidade]['quantidade']
                saida = {'quantidade': quantidade}
                return JsonResponse(saida)

    else:
        form = RemoveItem(auto_id=False)

    itens = []
    context = {'form': form}

    #query = Carrinho.objects.filter(user=request.user)
    itensCarrinho = carrinho.getCarrinho()
    for item in itensCarrinho:
        proj = Projeto.objects.get(pk=itensCarrinho[item]['id'])
        itens.append({'nome': proj.nomeProjeto, 'qtd': itensCarrinho[item]['quantidade'], 'id': itensCarrinho[item]['id']})        
    context['itens'] = itens

    return render(request, 'carrinho/carrinho.html', context)


def adiciona(request, idProjeto):
    carrinho = Carrinho(request)
    
    #item = Carrinho.objects.get(user=usuario, projeto=idProjeto)    
    #item.quantidade += 1
    carrinho.adicionar(idProjeto)
    response = 'carrinho alterado'
    
    return redirect('appsite:busca')