# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:49:26 2023

@author: hoshantm
"""

"""
sin(x) + 5*y - 78 = 0
4 * x + 7 * y - 34 = 0 
"""

from numpy import sin
from scipy.optimize import root

def f(v, a):
    x = v[0]
    y = v[1]
    
    return sin(x) + a*y - 78, 4 * x + 7 * y - 34 

x0 = 0.0 
y0 = 0.0
a = 5
for a in [4, 5, 6]:
    result = root(f, [x0, y0], args=(a,))
    print(f'Solution for a = {a} is x = {result.x[0]:0.4f} and {result.x[1]:0.4f}')
    
    
    
    