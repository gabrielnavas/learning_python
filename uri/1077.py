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
            is_char = True
            for op in ['*', '/', '+', '-', '^']:
                if ch == op:
                    is_char=False
                    break

            if is_char:
                fila.enqueue(ch)
            else:
                if ch != '(' and ch != ')':
                    if op == '':
                        op = ch
                    else:
                        while not fila.empty():
                            print(fila.front(), end='')
                            fila.deqeue()
                        print(op, end='')
                        op = ch

            while not fila.empty():
                print(fila.front())
                fila.deqeue()
            print(op, end='')

        n -= 1
        print()

process()