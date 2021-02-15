#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:01:24 2020

@author: user
"""
import pandas as pd
import numpy as np
import csp_def
import CA3
import backtracking


def data_aslist(data):
    f_list = []
    for i in range(len(data)):
        da = []
        for l in data[i]:
            da.append(l)
        f_list.append(da)
    
    return f_list

def main():
    data = pd.read_csv('sudokus_start.txt', header = None)
    np_data = data[0]
    f_list = data_aslist(np_data)
    solution = []
    for i in range(len(f_list)):
        csp = csp_def.csp_class(f_list[i])
        if CA3.issolved(csp):
            s = [csp.domain,' CA3']
            solution.append(s)
        else:
            data_f = backtracking.row_split(f_list[i])
            result = backtracking.backtrack(data_f)
            if result == True:
                s = [data_f,' BTS']
                solution.append(s)
         
    return solution

