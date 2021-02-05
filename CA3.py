#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:29:39 2020

@author: user
"""
import queue

def arc_builder(csp):
    
    arc = queue.Queue()
    for i in range(len(csp.variable)):
        for l in range(len(csp.constrains[csp.variable[i]])):
            if csp.variable[i] != csp.constrains[csp.variable[i]][l]:
                arc.put([csp.variable[i],csp.constrains[csp.variable[i]][l]])   
    
    return arc

def Revise (csp, Xi, Xj):
    rev = False
    values = csp.domain[Xi]
    for x in values:
        if not isconsistane(csp,x,Xi,Xj):
            csp.domain[Xi].remove(x)
            rev = True
    
    return rev

def isconsistane(csp,x,Xi,Xj):
    for y in csp.domain[Xj]:
        if Xj in csp.constrains[Xi] and y!= x:
            return True
        
    return False

def ca3(csp):
    
    arc = arc_builder(csp)
    while not arc.empty():
        (Xi,Xj) = arc.get()
        if Revise(csp, Xi, Xj):
            if len(csp.domain[Xi])==0:
                return False
            
            peers = csp.constrains[Xi]
            for i in peers:
                arc.put([i,Xi])
                
    return True
        
def issolved(csp):
    
    if not ca3(csp):
        return False
    else:
        for i in csp.variable:
            if len(csp.domain[i]) != 1:
                return False
    return True