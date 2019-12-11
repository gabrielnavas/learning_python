#errado

class Fila:

    def __init__(self):
        self.fila = []
        self.len=0

    def init(self):
        self.fila.clear()
        self.len=0

    def enqueue(self, e):
        self.fila.append(e)
        self.len += 1

    def deqeue(self):
        self.fila.pop(0)
        self.len -= 1

    def empty(self):
        return self.len == 0

    def front(self):
        return self.fila[0]

    def back(self):
        return self.fila[-1]


def process():
    n = int(input())
    fila = Fila()
    op = ''

    while n > 0:
        fila.init()

        expr = input()
        for ch in expr:
            if ch == '*' or ch == '/' or ch == '+' or ch == '-':
              if op != '':
                fila.enqueue(ch)
                while not fila.empty():
                    elem = fila.front()
                    fila.deqeue()
                    print(elem, end='')
                print(op, end='')
                op = ch
              
            elif ch != '(' and ch != ')':
              fila.enqueue(ch)
        n -= 1

process()
