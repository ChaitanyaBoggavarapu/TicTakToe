# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:42:32 2021

@author: abhil
"""

from prettytable import PrettyTable

def print_table(l):
    table = PrettyTable(['Col1', 'Col2', 'col2'])
    for rec in l:
        table.add_row(rec)
        
    print(table)