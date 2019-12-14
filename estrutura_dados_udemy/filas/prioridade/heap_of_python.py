import  heapq

class Pessoa:

    def __init__(self, nome=''):
        self.nome = nome

    def __repr__(self):
        return self.nome

class FilaPrioridade:

    def __init__(self):
        self._fila =  []
        self._indice = 0

    def inserir(self, item, prioridade):
        # -prioridade para ser uma fila max heap
        # _indice faz que os itens sejam ordenados com a ordem que foram inseridos
        heapq.heappush(self._fila, (-prioridade, self._indice, item))
        self._indice += 1

    def remover(self):
        return heapq.heappop(self._fila)[-1]


if __name__ == '__main__':
    fila = FilaPrioridade()

    fila.inserir(Pessoa('Gabriel'), 20)
    fila.inserir(Pessoa('Navas'), 16)
    fila.inserir(Pessoa('Rafael'), 18)
    fila.inserir(Pessoa('Ana'), 14)
    fila.inserir(Pessoa('João'), 16)

    print(fila.remover())
    print(fila.remover())

