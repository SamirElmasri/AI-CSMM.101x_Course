#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:30:06 2020

@author: user
"""

def row_split(data):
    rows = []
    row = []
    nd = []
    for i in data:
        nd.append(int(i))
        
    for i in range(9):
        for l in range(9):
            row.append(nd[l+i*9])
        rows.append(row)
        row = []
    return rows
 
def next_cell(data_f):
    
    for i in range(9):
        for l in range(9):
            if data_f[i][l] == 0:
                return i , l
            
    return None, None

def valid(data_f,poss,row,column):
    
    rowvalue = data_f[row]
    if poss in rowvalue:
        return False 
    colvalue = []
    for i in range(9):
        colvalue.append(data_f[i][column])
    if poss in colvalue:
        return False
    rowst = (row // 3) * 3 
    colst = (column // 3) * 3
    for i in range(rowst, rowst + 3):
        for l in range(colst, colst + 3):
            if data_f[i][l] == poss:
                return False

    return True

def backtrack(data_f):
    
    row,column = next_cell(data_f)
    if row == None or column == None:
        return True
    
    for poss in range(10):
        if valid(data_f,poss,row,column):
            data_f[row][column] = poss
            if backtrack(data_f):
                return True
    
    data_f[row][column] = 0
    
    return False


    