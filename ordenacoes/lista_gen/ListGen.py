from ordenacoes.lista_gen.MyStack import MyStack
from ordenacoes.lista_gen.No import No
from ordenacoes.lista_gen.Info import Info

class ListGen:

    def __init__(self):
        self.starter = None

    def restart(self):
        self.starter = None

    def insertStr(self, str: ""):

        stack = MyStack()
        no = None
        info = ""
        i = 0
        j = 0

        self.starter = self._cons(None, None)
        i += 1

        stack.push(self.starter)

        while not stack.isEmpty() and i < len(str):

            # get characters
            if str[i] != ']' and str[i] != '[' and str[i] != ',' and i < len(str):
                info = ""
                j=0

                while i < len(str) and str[i] != ']' and str[i] != ',':
                    i = self._nextPointDispenseSpace(str, i)
                    info[i] = str[i]
                    i += 1
                    j += 1

                no.head = self._createTerminal(info)

                i = self._nextPointDispenseSpace(str, i)

                # get head
                if str[i] == '[':
                    no.head = self._cons(None, None)
                    stack.push(no.head)
                    no = no.head
                    i += 1

                i = self._nextPointDispenseSpace(str, i)

                # get tail
                if str[i] == ',':
                    stack.pop() # get top
                    no.tail = self._cons(None, None) # new tail in no
                    stack.push(no.tail) # stacking tail
                    no = no.tail #get tail of no
                    i += 1

                i = self._nextPointDispenseSpace(str, i)

                # get get end
                if str[i] == ']':
                    stack.pop() # finish, get curret no and backup

                    if not stack.isEmpty():
                        no = no.top()

                    i += 1

    def _nextPointDispenseSpace(self, str: str, position: int):
        """
        go to next character skipping spaces

        :param str: current string
        :param position: string position
        :return: position that is not space character
        """

        while(position < len(str) and str[position] == ' '):
            position += 1

        return position

    def show(self):

        if self._isNone(self.starter):
            print("[]")
        else:
            self._show(self.starter)

    def _show(self, no):

        if no != None:
            if self._isAtom(no):
                print(no.info)
            else:
                print("[", end='')

                while(not self._isNone(no)):
                    self._show(self.head(no))

                    no = self._tail(no)
                    if not self._isNone(no):
                        print(", ")

                print("]")

    def _cons(self, head, tail):
        new_no = None

        if self._isAtom(tail):
            print("tail cannot be terminal")
        else:
            new_no = No(head, tail)

        return new_no

    def _head(self, no):
        return_no = None

        if self.isNone(no) or self.isAtom(no):
            print("no cannot be None or Atom")
        else:
            return_no = no.head()

        return return_no

    def _createTerminal(self, info: str):
        return Info(str)

    def _isNone(self, no):
        return no == None

    def _isAtom(self, no):
        return not self._isNone(no) and isinstance(no, Info)
