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
        self.grafo[u].append(u)

    
    def isLigacao(self, u, v):
        return v in self.grafo        
    
    def show(self):
        k=0
        for i in self.grafo:
            print('{}:'.format(k), end=' ')
            for j in i:
                print('{} -> '.format(j), end='')
            print() 
            k += 1
            
g = Grafo(5)
g.add_aresta(0, 1)
g.add_aresta(0, 3)
g.add_aresta(1, 0)
g.add_aresta(1, 2)
g.add_aresta(1, 4)
g.add_aresta(2, 1)
g.add_aresta(2, 4)
g.add_aresta(3, 0)
g.add_aresta(4, 1)
g.add_aresta(4, 2)
g.show()            