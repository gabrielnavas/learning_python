#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:09:11 2019

@author: navas
"""

class Grafo:
    
    """
    Grafo não direcionado (nao dirigido)
    """
    
    def __init__(self, vertices):
        self.vertices = vertices
        
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]                
        self.visitados = [False]*self.vertices        
        
        
    def add_aresta(self, u, v):
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
        return self.grafo[u][v] == 1        
    
            
    def dfs(self, u):
        self.visitados[u] = True
        print('{} visitado.'.format(u))
        for i in range( self.vertices):
            if self.grafo[u][i] == 1 and self.visitados[i] == False:
                self.dfs(i)
        
        
g = Grafo(5)

print(g.isLigacao(0, 1))
g.add_aresta(0, 2)
g.add_aresta(1, 2)
g.add_aresta(2, 0)
g.add_aresta(2, 1)
g.add_aresta(2, 3)
g.add_aresta(2, 4)
g.add_aresta(4, 2)
g.add_aresta(4, 3)            

g.dfs(0)
g.showMatrix()