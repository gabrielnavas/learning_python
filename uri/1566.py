#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:40:18 2019

@author: navas
"""


n = int(input())
while n > 0:
    
    n_nums = int(input())
    
    
    lista = list(filter(lambda i: i >= 20 and i <=230, map(int, input().rsplit(' '))))
        
    lista.sort()
    for i in lista:
        print(i, sep=' ')
    
    n -=1