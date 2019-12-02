from ordenacoes.lista_gen.NoStack import NoStack


class MyStack:
    def __init__(self):
        self.starter = None

    def restart(self):
        self.starter = None

    def push(self, item):
        new_no = NoStack(item, self.starter)
        self.starter = new_no

    def pop(self):
        return_no = self.starter.item
        self.starter = self.starter.prox

        return return_no

    def isEmpty(self):
        return self.starter == None

    def top(self):
        return self.starter.item

    def showStack(self):
        no = self.starter

        print("[", end='')
        while no != None:

            if no.next == None:
                print("{}".format(str(no.item)), end='')
            else:
                print("{}, ".format(str(no.item)), end='')

            no = no.next

        print("]")

if __name__ == '__main__':

    s = MyStack()

    for n in range(0, 11):
        s.push(n)

    s.showStack()

