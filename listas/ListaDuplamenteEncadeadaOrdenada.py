class No:
    def __init__(self, info=None, ante=None, prox=None):
        self.ante=ante
        self.prox=prox
        self.info=info


class ListaDuplamenteEncadeadaOrdenada:
    def __init__(self):
        self.cabeca = None
        self.rabo = None

    def inserir(self, info):
        novo = No(info, None, None)

        if(self.cabeca  == None):
            self.cabeca =  novo
            self.rabo = novo

        elif(info < self.cabeca.info):
            novo.prox = self.cabeca
            self.cabeca.ante = novo
            self.cabeca = novo

        elif(info > self.rabo.info):
            novo.ante = self.rabo
            self.rabo.prox = novo
            self.rabo = novo

        else:
            aux = self.cabeca.prox
            while(info > aux.info):
                aux = aux.prox

            novo.prox = aux
            novo.ante = aux.ante
            aux.ante = novo
            aux.ante.prox=novo

    def exibir(self):
        aux=self.cabeca
        while(aux is not None):
            print(aux.info, end=' ')
            aux=aux.prox

if __name__ == '__main__':
    listaOrd = ListaDuplamenteEncadeadaOrdenada()

    for i in [20,1,4,3,30, 15]:
        listaOrd.inserir(i)

    listaOrd.exibir()