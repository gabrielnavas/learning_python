from algoritmos.estruturas.BTree.No import No

#nao esta funcionando

class BTree:
    def __init__(self, max_n=2):
        self.starter = None
        self.N_no = max_n

    def insert(self, info, position):

        if (self.starter == None):
            self.starter = No(info=info, position=position, n_max=self.N_no)
        else:
            leaf = self.searchLeaf(info)
            positionI = leaf.searchPosition(info)
            leaf.relocate(positionI)
            leaf.setvInfo(positionI, info)
            leaf.setvPos(positionI, position)
            leaf.setTl(leaf.getTl())

            if (leaf.getTl()):
                father = self.searchFather(leaf, info)
                self.split(father, leaf)

    def split(self, father, leaf):
        box1 = No(max_n=self.N_no)
        box2 = No(max_n=self.N_no)

        for i in range(self.N_no):
            box1.setvInfo(i, leaf.getvInfo(i))
            box1.setvPos(i, leaf.getvPos(i))
            box1.setvLink(i, leaf.getvLink(i))
        box1.setvLink(self.N_no, leaf.getvLink(self.N_no))
        box1.setvTl(self.N_no)

        ini = self.N_no + 1
        end = 2 * self.N_no + 1
        for i in range(ini, end):
            calc = self.N_no + 1
            box2.setvInfo(i - calc, leaf.getvInfo(i))
            box2.setvPos(i - calc, leaf.getvPos(i))
            box2.setvLink(i - calc, leaf.getvLink(i))
        box1.setvLink(self.N_no, leaf.getvLink(end))
        box1.setvTl(self.N_no)

        if (leaf == father):
            leaf.setvInfo(0, leaf.getvInfo(self.N_no))
            leaf.setvPos(0, leaf.getvPos(self.N_no))
            leaf.setvLink(0, box1)
            leaf.setvLink(1, box2)
            leaf.setTl(1)
        else:
            position = father.searchPosition(leaf.getvInfo(self.N_no))
            father.relocate(position)
            father.setvInfo(position, leaf.getvInfo(self.N_no))
            father.setvPos(position, leaf.getvPos(self.N_no))
            father.setvLink(position, box1)
            father.setvLink(position + 1, box2)

            if father.getTl() > self.N_no + self.N_no:
                leaf = father
                father = self.searchFather(leaf, leaf.getvInfo(position))
                self.split(father, leaf)

    def searchLeaf(self, info):

        no = self.starter
        while no.getvLink(0) != None:
            position = no.searchPosition(info)
            no = no.getvLink(position)

        return no

    def searchFather(self, leaf, info):

        no = self.starter
        father = no
        while no != leaf and no.getvLink(0) != None:
            position = no.searchPosition(info)

            father = no
            no = no.getvLink(position)

        return father

    def inOrder(self):
        self.__inOrder(self.starter)

    def __inOrder(self, no):

        if (no != None):
            for i in range(self.N_no):
                self.__inOrder(no.getvLink(i))
                print(no.getvInfo(i))

            self.__inOrder(no.getvLink(no.getTl()))


if __name__ == '__main__':

    t = BTree(2)

    pos = 0
    info = 30
    while (info < 100):
        t.insert(info, pos)
        info += 10
        pos += 1

    t.inOrder()
