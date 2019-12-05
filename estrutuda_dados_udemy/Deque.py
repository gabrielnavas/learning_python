class No:

    def __init__(self, info=None, prev=None, next_no=None):
        self.info = info
        self.prev = prev
        self.next_no = next_no

    def getNext(self):
        return next_no

    def show(self, cont=None):
        print("[{} {}, {}, {}]".format(cont if cont is not None else '',
              self.info, self.prev, self.next_no))


class Deque:

    def __init__(self):
        self.len = 0
        self.end = None
        self.starter = None

    def restart(self):
        self.starter = None
        self.end = None
        self.len = 0

    def empty(self):
        return self.len == 0

    def enqueue_front(self, elem):
        new_no = No(info=elem, next_no=self.starter)

        if self.starter is None:
            self.starter = new_no
            self.end = new_no
        else:
            self.starter.prev = new_no
            self.starter = new_no
        self.len += 1

    def enqueue_back(self, elem):

        new_no = No(info=elem, prev=self.end)

        if self.end is None:
            self.starter = new_no
            self.end = new_no
        else:
            self.end.prox = new_no
            self.end = new_no
        self.len += 1

    def dequeue_front(self):
        elem = self.starter.info

        if self.starter == self.end:
            self.starter = None
            self.end = None
        else:
            self.starter = self.starter.prox
            self.starter.prev = None

        self.len -= 1
        return elem

    def dequeue_back(self):
        elem = self.end.info

        if self.starter == self.end:
            self.starter = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.prox = None


        self.len -= 1
        return elem

    def showAll(self):
        i = 0
        no = self.starter
        while no is not None:
            no.show(cont=i)
            no = no.getNext()
            i += 1


d = Deque()

for i in range(10, 30):
    d.enqueue_back(i)
d.showAll()
