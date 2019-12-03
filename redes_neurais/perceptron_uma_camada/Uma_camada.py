#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:55:21 2019

@author: navas
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    
    for i in range(3):
        s += e[i] * p[i]
        print(s)
    
    return s


s = soma(entradas, pesos)


def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)