from appsite.models import Projeto

class Carrinho(object):
    def __init__(self, request):
        self.session = request.session
        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        
        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}


    def adicionar(request, id, quantidade=1):
        projeto = Projeto.objects.get(pk=id)
        projeto_id = str(id)            

        if projeto_id not in self.carrinho:
            self.carrinho[projeto_id] = {'id': str(projeto.id), 'quantidade': quantidade}

        else:
            #nao sei pq essa linha
            self.carrinho[projeto_id]['quantidade'] = quantidade

        self.salvar()


    def remover(request, id):
        projeto_id = str(id)

        if projeto_id in self.carrinho:
            del self.carrinho[projeto_id]
            self.salvar()


    def alterar(request, id, quantidade):
        projeto_id = str(id)

        if projeto_id in self.carrinho:
            self.carrinho[projeto_id]['quantidade'] = quantidade
            self.salvar()

    def salvar():
        self.session[setting.CARRINHO_SESSION_ID] = self.carrinho