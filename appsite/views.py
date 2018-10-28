from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ProjetoForm
#from appsite.models import Image

def teste(request):
    return HttpResponse("Servidor ativo")

def index(request):
    return render(request, 'appsite/index.html')

def signIn(request):
    return render(request, 'appsite/sign_in.html')

def signUp(request):
    #imagem = get_object_or_404(Image, pk=2)
    return render(request, 'appsite/sign_up.html')

def cadastro(request):

    form = ProjetoForm()
    context = {'form': form, }
    return render(request, 'appsite/cadastro.html', context)

def exibe(request):
    pass

def edita(request):
    pass

def remove(request):
    pass