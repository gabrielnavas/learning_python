#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque

class Grafo:
    # class Fila:
    #     def __init__(self):
    #         self._stack = deque()
    #         self._top = -1
    #
    #     def push(self, e):
    #         self._stack.append(e)
    #         self._top += 1
    #
    #     def pop(self):
    #         self._stack.pop()
    #         self._top -= 1
    #
    #     def top(self):
    #         return self._stack[self._top]
    #
    #     def empty(self):
    #         return self._top == -1

    """
    Grafo não direcionado (nao dirigido)
    """

    def __init__(self, vertices):
        self.vertices = vertices

        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        # self.visitados = [False]*self.vertices


    def add_aresta(self, u, v):
        u, v = u-1, v-1
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def showPairs(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print("({}, {})".format(i, j))

    def showMatrix(self):
        for i in self.grafo:
            for j in i:
                if j == 0 or j != len(i)-1:
                    print(' {}, '.format(j), end='')
            print()

    def isLigacao(self, u, v):
        u, v = u - 1, v - 1
        return self.grafo[u][v] == 1


    def dfs(self, u) -> None:
        """
        Busca em profundidade

        :param u:
        :return None:
        """

        visitados = [False for _ in range(self.vertices)]

        def _dfs_rec(u: int, visitados: []) -> None:
            u=-1
            self.visitados[u] = True
            print('{} visitado.'.format(u+1))
            for i in range(self.vertices):
                if self.grafo[u][i] == 1 and not self.visitados[i]:
                    _dfs_rec(i, visitados)

        _dfs_rec(u, visitados)

    def bfs(self, v):
        """
            busca em largura, usando fila.
        :param v:
        :return:
        """

        # lista de visitados
        visitados = [False] * self.vertices

        # marca 'v' como visitado
        visitados[v] = True

        # insere 'v' na fola
        fila = [v]

        while len(fila) > 0:

            # obtem o elemento da fila
            v = fila[0]

            # para cada vertice 'u' adjacente a 'v'
            for u in range(self.vertices):
                # verifica se existe conexao
                if self.grafo[v][u] == 1:
                    # verifica se 'u' não foi visitado
                    if visitados[u] == False:
                        # marca 'u' como visitado
                        visitados[u] = True
                        # insere 'u' na fila
                        fila.append(u)
                        # imprime o elemento visitado
                        print('visitado {}'.format(u))

            # remove 'v' da fila
            fila.pop(0)


if __name__ == '__main__':

    # g = Grafo(5)
    #
    # print(g.isLigacao(0, 1))
    # g.add_aresta(0, 2)
    # g.add_aresta(1, 2)
    # g.add_aresta(2, 0)
    # g.add_aresta(2, 1)
    # g.add_aresta(2, 3)
    # g.add_aresta(2, 4)
    # g.add_aresta(4, 2)
    # g.add_aresta(4, 3)
    #
    # g.dfs(0)
    # g.showMatrix()

    g2 = Grafo(10)

    g2.add_aresta(1, 2)
    g2.add_aresta(1, 3)
    g2.add_aresta(1, 4)
    g2.add_aresta(2, 5)
    g2.add_aresta(3, 6)
    g2.add_aresta(3, 7)
    g2.add_aresta(4, 8)
    g2.add_aresta(5, 9)
    g2.add_aresta(6, 10)
    # g2.showMatrix()
    g2.bfs(1)