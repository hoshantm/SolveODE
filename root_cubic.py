# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:48:40 2023

@author: hoshantm
"""
from scipy.optimize import root, minimize
import numpy as np

import matplotlib.pyplot as plt

def f(x, a, b, c, d):
    return a * x**3 + b * x **2 + c * x + d 

def g(x, a, b, c, d):
    return -f(x, a, b, c, d)


def fprime(x, a, b, c, d):
    return 3 * a * x**2 + 2 * b * x + c
    
# Roots: 3, -5 and -8

a = 1
b = 10
c = 1
d = -120
x0 = -10
result = root(f, x0, args=(a, b, c, d), jac=fprime)
print(f'Solution = {result.x[0]:0.4f} radians or {np.rad2deg(result.x[0]):0.2f} degrees')
print(f'{result.nfev - 1} function evaluations.')
try:
    print(f'{result.njev} jacobian evaluations.')
except:
    pass
print('\n')


x = np.linspace(-9, 4, 360)
y = f(x, a, b, c, d)
plt.plot(x, y)
plt.scatter([result.x[0]], [a], color='red')
plt.grid()
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

print(result)