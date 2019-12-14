#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#cdogio está errado!!!!


class Person():
    def __init__(self, index=0, nome = ''):
        self.index = index
        self.nome = nome
        
    def getIndex(self):
        return self.index

    def getNome(self):
        return self.nome        
    
    def toStr(self):
        return '{}, {}'.format(self.index, self.nome)

class FilaPriori():
    
    def __init__(self):
        self.fila=[]
        self.len = 0
        
    def insert(self, obj):
                
        if(self.len == 0):
            self.fila.append(obj)
        else:
            i=0
            while i < self.len and obj.getIndex() > self.fila[i].getIndex():
                i += 1
                
            self.fila.insert(i, obj)
        
        self.len += 1
     
    def pop(self, index):
        
        if len(self.fila) > 0 and index >= 0 and index < self.len:
            self.fila.pop(index)
            self.len -= 1
            
    def front(self):
        return self.fila[0]

    def back(self):
        return self.fila[-1]        
        
    def show(self):
        for i in range(self.len):
            print(self.fila[i].toStr())
 
f = FilaPriori()
f.insert(Person(7, 'gabriel'))
f.insert(Person(5, 'gabriel'))
f.insert(Person(3, 'gabriel'))
f.insert(Person(1, 'gabriel'))
f.show()

             