class No:
    def __init__(self, info=None, ante=None, prox=None):
        self.ante=ante
        self.prox=prox
        self.info=info


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.rabo = None


    def inserir(self, info):

        novo = No(info, None, None)

        if(self.cabeca == None):
            self.cabeca = novo
            self.rabo = novo
        else:
            self.rabo.prox = novo
            novo.ante = self.rabo
            self.rabo = novo

    def remover(self, info):
        aux=self.cabeca

        while(aux != None and aux.info != info):
            aux = aux.prox

        return aux

    def exibir(self):
        aux = self.cabeca
        while(aux != None):
            print(aux.info, end=' ')
            aux=aux.prox


if __name__ == '__main__':
    lista = ListaDuplamenteEncadeada()


    for i in [10,30,5,4,29]:
        lista.inserir(i)

    lista.exibir()
