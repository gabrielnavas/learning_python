#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#errado
notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}


str = input()
while str is not '*':
    tot = 0.0
    
    for ch in str:
        if ch != '/':
            print('{}, {}'.format(ch, notas[ch]))
            tot += float(notas[ch])
            
    print('{:.0f}'.format(tot))
    str = input()        