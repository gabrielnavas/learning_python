class Tree:
    def __init__(self, info, esq=-1, dir=-1):
        self.info=info
        self.esq=esq
        self.dir=dir


def inserir(tree = [], info=None):
    novo = Tree(info)

    if(len(tree) == 0):
        tree.append(novo)
    else:
        flag=False
        aux = tree[0]

        while(flag is False):
            if(info < aux.info):
                if(aux.esq != -1):
                    aux = tree[aux.esq]
                else:
                    flag=True
            else:
                if(aux.dir != -1):
                    aux = tree[aux.dir]
                else:
                    flag = True

        if(info < aux.info):
            aux.esq = len(tree)
        else:
            aux.dir = len(tree)

        tree.append(novo)

    return tree

def exibir_pre(tree, pos=0):
    if(len(tree) > 0 and pos != -1):
        print(tree[pos].info, end=' ')
        exibir_pre(tree, tree[pos].esq)
        exibir_pre(tree, tree[pos].dir)

def exibir_in(tree, pos=0):
    if (len(tree) > 0 and pos != -1):
        exibir_pre(tree, tree[pos].esq)
        print(tree[pos].info, end=' ')
        exibir_pre(tree, tree[pos].dir)


def exibir_pos(tree, pos=0):
    if (len(tree) > 0 and pos != -1):
        exibir_pre(tree, tree[pos].esq)
        exibir_pre(tree, tree[pos].dir)
        print(tree[pos].info, end=' ')

def buscar(tree=[], pos=0, info=None):

    if(len(tree) > 0 and pos != -1):

        flag = False
        aux = tree[0]

        while (flag is False):
            # pai = pos
            if (info < tree[pos].info):
                if (tree[pos].esq != -1):
                    pos = tree[aux.esq]
                else:
                    flag = True
            else:
                if (aux.dir != -1):
                    aux = tree[aux.dir]
                else:
                    flag = True


# return False, -1, -1

tree = []

for i in [100,120,110, 130, 90, 80]:
    tree = inserir(tree, i)

for i in tree:
    print(i.info, end=' ')

print("\n\npre-order")
exibir_pre(tree)

print("\npos-order")
exibir_in(tree)

print("\npos-order")
exibir_pos(tree)
