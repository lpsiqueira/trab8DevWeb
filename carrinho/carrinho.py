from appsite.models import Projeto
from projeto import settings

class Carrinho(object):
    def __init__(self, request):
        self.session = request.session
        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        
        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

    
    def getCarrinho(self):
        return self.carrinho


    def adicionar(self, id):
        projeto = Projeto.objects.get(pk=id)
        projeto_id = str(id)            

        if projeto_id not in self.carrinho:
            self.carrinho[projeto_id] = {'id': projeto.id, 'quantidade': 1}

        else:
            self.carrinho[projeto_id]['quantidade'] += 1

        self.salvar()


    def remover(self, id):
        projeto_id = str(id)

        if projeto_id in self.carrinho:
            del self.carrinho[projeto_id]
            self.salvar()


    def alterar(self, id, quantidade):
        projeto_id = str(id)

        if projeto_id in self.carrinho:
            self.carrinho[projeto_id]['quantidade'] = quantidade
            self.salvar()

    def salvar(self):
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho