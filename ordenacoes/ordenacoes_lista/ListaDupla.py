class No:
    def __init__(self, info, prev, prox):
        self.info = info
        self.prev = prev
        self.prox = prox

    def show(self):
        print(self.info)

class ListaDupla:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tl=0

    def init_now(self):
        self.inicio = None
        self.fim = None
        self.tl = 0

    def insert(self, info):

        novo = No(info, self.fim, None)

        if(self.fim == None):
            self.inicio = novo
            self.fim = novo
            self.tl=1
        else:
            self.fim.prox = novo
            self.fim = novo
            self.tl =self.tl + 1

    def show(self):

        no = self.inicio

        while(no != None):
            no.show()
            no = no.prox

    def directInsert(self):

        aux=0
        noI: No=None
        noPos:No = None

        noI=self.inicio
        while(noI != self.fim):

            noPos = noI.prox
            aux = noPos.info

            while(noPos != self.inicio and noPos.prev.info > aux):
                noPos.info = noPos.prev.info
                noPos = noPos.prev

            noPos.info = aux
            noI = noI.prox

    def noNext(self, number, noInit:No):

        while(number):
            noInit = noInit.prox
            number = number-1

    def noPrev(self, number, noInit: No):

        while (number):
            noInit = noInit.ant
            number = number - 1

    def binarySearch(self, key):

        ini=0
        end=self.tl-1
        middle = end/2

        no = self.noNext(middle, self.inicio)

        while(ini < end and key != no.info != no.info):

            if(key > no.info):
                ini = middle+1
            else:
                end = middle-1

            middle = (ini+end)/2
            no = self.noProx(middle, self.inicio)

        if(ini < end and key == no.info):
            return no
        return None

if __name__ == '__main__':
    l = ListaDupla()

    l.insert(5)
    l.insert(2)
    l.insert(7)
    l.insert(6)
    l.insert(8)
    l.insert(10)
    l.insert(1)

    # l.directInsert()

    print(l.binarySearch(7))

    l.show()