from ordenacoes.lista_gen.NoGen import NoGen


class No(NoGen):

    def __init__(self):
        self._head=None
        self._tail=None

    def __init__(self, head, tail):
        self._head = head
        self._tail = tail

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail):
        self._tail = tail