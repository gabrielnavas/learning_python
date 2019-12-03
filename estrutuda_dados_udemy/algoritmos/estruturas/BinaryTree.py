class No:
    def __init__(self, left=None, right=None, label=None):
        self.right = right
        self.left = left
        self.label = label


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        newNo = No(label=label)

        if self.root == None:
            self.root = newNo
        else:
            no_aux = self.root
            prev = None

            while no_aux != None:
                prev = no_aux

                if label < no_aux.label:
                    no_aux = no_aux.left
                else:
                    no_aux = no_aux.right

            if label < prev.label:
                prev.left = newNo
            else:
                prev.right = newNo

    def inOrder(self):

        def inOrdem(no):
            if no != None:
                inOrdem(no.left)
                print(no.label)
                inOrdem(no.right)

        inOrdem(self.root)

    def inOrderInverter(self):

        def inOrdem(no):
            if no != None:
                inOrdem(no.right)
                print(no.label)
                inOrdem(no.left)

        inOrdem(self.root)

    def preOrder(self):

        def preOrdem(no):
            if no != None:
                print(no.label)
                preOrdem(no.left)
                preOrdem(no.right)

        preOrdem(self.root)

    def posOrder(self):

        def posOrder(no):
            if no != None:
                posOrder(no.left)
                posOrder(no.right)
                print(no.label)

    def searchNoAndFather(self, label):

        no = self.root
        father = no

        while no != None and no.label != label:
            father = no

            if label < no.label:
                no = no.left
            else:
                no = no.right

        return no, father

    def remove(self, no, father):

        # is leaf
        if no.left != None and no.right != None:
            if no != father:
                if no.label > father.label:
                    father.right = None
                else:
                    father.left = None
            else:
                self.root = None
        elif no.left == None or no.right == None:
            # 1 son
            if no != father:
                if no.label > father.label:
                    if no.right == None:
                        father.right = no.left
                    else:
                        father.right = no.right
                else:
                    if no.right == None:
                        father.left = no.left
                    else:
                        father.right = no.right
            else:
                if no.left == None:
                    self.root = no.right
                else:
                    self.root = no.left
        else:
            # 2 son
            sub = no.dir
            fatherSub = no
            while sub.left != None:
                fatherSub = sub
                sub = sub.left

            no.label = sub.label
            sub.label += 1

            self.remove(sub, fatherSub)


if __name__ == '__main__':
    bt = BinaryTree()

    for i in range(30, 50):
        bt.insert(i)

    for i in range(30, 49):
        no, father = bt.searchNoAndFather(i)
        bt.remove(no, father)

    print("in order inverter")
    bt.inOrderInverter()
