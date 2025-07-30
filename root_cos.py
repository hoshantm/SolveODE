# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:45:07 2023

@author: hoshantm
"""
from scipy.optimize import root
import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
    return np.cos(x) - a

def fprime(x, a):
    return -np.sin(x)
    
x0 = np.pi / 2
a = 0.5
result = root(f, x0, args=(a,), jac=fprime)
print(f'Solution = {result.x[0]:0.4f} radians or {np.rad2deg(result.x[0]):0.2f} degrees')
print(f'{result.nfev - 1} function evaluations.')
try:
    print(f'{result.njev} jacobian evaluations.')
except:
    pass
print('\n')


x = np.linspace(-2 * np.pi, 2 * np.pi, 360)
y = f(x, 0)
plt.plot(x, y)
plt.scatter([result.x[0]], [a], color='red')
plt.grid()

print(result)