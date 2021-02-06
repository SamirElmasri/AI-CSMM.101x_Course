#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:18:07 2020

@author: user
"""

class csp_class:
    
   def __init__(self,data):
        rows = [1,2,3,4,5,6,7,8,9]
        columns = ['a','b','c','d','e','f','g','h','i']
        variable = cross(rows,columns)
        self.variable = variable
        domain = dom(data,variable,rows)
        self.domain = domain
        row_cross = []
        column_cross = []
        for r in rows:
            row_cross.append(cross_n(r,columns))
        for c in columns:
            column_cross.append(cross_str(rows,c))
        square_cross = sq_cross()
        utilities = [row_cross,column_cross,square_cross]
        self.utilities = utilities
        peers = peers_builder(variable,utilities)
        self.peers = peers
        constrains = cons_builder(variable,peers)
        self.constrains = constrains
        
def cross(a,b):
    crossing = []
    for i in b:
        for l in a:
            crossing.append(str(i)+str(l))
    
    return crossing

def cross_n (a,b):
    
    crossing = []
    for i in b:
        crossing.append(str(i)+str(a))
        
    return crossing

def cross_str (a,b):
    
    crossing = []
    for i in a:
        crossing.append(str(b)+str(i))
        
    return crossing

def dom(data,variable,X):
    
    dom = dict()
    for i in range(len(data)):
        if data[i] != str(0):
            dom.update({variable[i] : [data[i]]})
        else:
            dom.update({variable[i]: [str(x) for x in X]})
            
    return dom

# 3x3 square
def sq_cross():
    
    rows = [[1,2,3],[4,5,6],[7,8,9]]
    columns = [['a','b','c'],['d','e','f'],['g','h','i']]
    square_cross = []
    for c in columns:
        for r in rows:
            square_cross.append(cross(r,c))
            
    return square_cross

#build the original peers and output 3 array with peers in columns rows and 3x3 squares
def peers_builder(variable,utilities):
    
    peers = {}
    for i in range(len(variable)):
        up = []
        for l in range(len(utilities)):
            for n in range(len(utilities[l])):
                if variable[i] in utilities[l][n]:
                    up.append(utilities[l][n])
        peers.update({variable[i] : up})
                    
    return peers

#build the initial constrains
def cons_builder(variable,peers):
    
    cons = dict()
    for i in range(len(variable)):
        li = []
        for l in peers[variable[i]]:
            for m in l:
                li.append(m)
# removes the same variable in the constrains
        li.remove(variable[i])
        li.remove(variable[i])
        li.remove(variable[i])
        cons.update({variable[i]:li})
    
    return cons
                    