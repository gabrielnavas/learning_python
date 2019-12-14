#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:54:16 2019

@author: navas
"""


class Grafo:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(vertices)]

    def add_aresta(self, u, v):
        self.grafo[u].append(v)

    
    def isLigacao(self, u, v):
        return v in self.grafo        
    
    def show(self):
        k=0
        for i in self.grafo:
            print('{}:'.format(k), end=' ')
            for j in i:
                print('{} -> '.format(j), end='')
            print('\\')
            k += 1

    def dfs(self, u: int) -> None:
        """
            Busca em profundidade
        :param u:
        :return:
        """
        visitados = [False for _ in range(self.vertices)]

        def __dfs(u: int, visitados: []) -> None:
            for i in range(self.vertices):
                if not visitados[u]:
                    visitados[u] = True
                    print('{} visitado'.format(visitados[u]))
                    for j in range(self.grafo[i]):
                        __dfs(j, visitados)
        __dfs(u, visitados)

    def bfs(self, v: int):

        visitados = [False] * self.vertices
        fila = [v-1]

        while len(fila) > 0:

            v = fila[0]
            visitados[v] = True
            for u in range(self.vertices):
                if visitados[u] == False:
                    fila.append(self.grafo[v][u])
                    print('{} visitado'.format(u+1))

            fila.pop(0)



if __name__ == '__main__':

    # test 1
    # g = Grafo(5)
    # g.add_aresta(0, 1)
    # g.add_aresta(0, 3)
    # g.add_aresta(1, 0)
    # g.add_aresta(1, 2)
    # g.add_aresta(1, 4)
    # g.add_aresta(2, 1)
    # g.add_aresta(2, 4)
    # g.add_aresta(3, 0)
    # g.add_aresta(4, 1)
    # g.add_aresta(4, 2)
    # g.show()

    g2 = Grafo(4)
    g2.add_aresta(0, 3)
    g2.add_aresta(1, 2)
    g2.add_aresta(1, 3)
    g2.add_aresta(2, 3)
    g2.add_aresta(2, 1)
    g2.add_aresta(3, 0)
    g2.add_aresta(3, 0)
    g2.add_aresta(3, 1)
    g2.add_aresta(3, 2)
    g2.bfs(0)
    g2.show()