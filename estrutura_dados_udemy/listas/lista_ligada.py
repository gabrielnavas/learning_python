#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Dec  9 15:53:12 2019

@author: navas
"""

class NoSimple(object):

    def __init__(self, elem=None, nextNo=None):
        self.elem = elem
        self.nextNo = nextNo

    def setElem(self, e):
        self.elem = e

    def getElem(self):
        return self.elem

    def setNext(self, no):
        self.nextNo = no

    def getNext(self):
        return self.nextNo

    def show(self):
        print('{elem}, {next_no}'.format(elem=self.elem, next_no=self.nextNo))


class ListLinkedSimple(object):

    def __init__(self):
        self.starter = None
        self.end = None
        self.len = 0

    def insert(self, index, elem):
        new_no = NoSimple(elem=elem)
        if self.len == 0:
            self.starter = new_no
            self.end = new_no
        else:
            if index == 0:
                new_no.setNext(self.starter)
                self.starter = new_no
            elif index == self.len:
                self.end.setNext(new_no)
                self.end = new_no
            else:

                prev_no = self.starter
                curr_no = self.starter.getNext()

                i = 1
                while curr_no is not None and index > i:
                    prev_no = curr_no
                    curr_no = curr_no.getNext()
                    i += 1

                prev_no.setNext(new_no)
                new_no.setNext(curr_no)
        self.len += 1

    def pop(self, index):

        if index >= 0 and index < self.len:
            if index == 0 :
                if self.starter == self.end:
                    self.starter = None
                    self.end = None
                else:
                    self.starter = self.starter.getNext()
            else:
                prev_no = self.starter
                curr_no = self.starter.getNext()
    
                i = 1
                while curr_no is not None and index > i:
                    prev_no = curr_no
                    curr_no = curr_no.getNext()
                    i += 1
    
                if curr_no is not None and curr_no == self.end:
                    prev_no.setNext(None)
                    self.end = prev_no
                else:
                    prev_no.setNext(curr_no.getNext())
    
            self.len -= 1

    def front(self):
        return self.starter.getElem()

    def back(self):
        return self.end.getElem()

    def show(self):
        no = self.starter
        while no is not None:
            no.show()
            no = no.getNext()
            
    def length(self):
        return self.len        

if __name__ == '__main__':

    l = ListLinkedSimple()
    l.insert(0, 1)
    l.insert(0, 2)
    l.insert(1, 3)
    l.insert(4, 8)
    l.insert(3, 9)

    l.show()
    print('-----')
    l.pop(4)
    l.pop(3)
    l.pop(2)
    l.pop(1)
    l.pop(0)
    l.show()
    
    print('len: {}'.format(l.length()))
