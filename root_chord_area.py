# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:16:30 2023

@author: hoshantm
"""
from scipy.optimize import root
import numpy as np
import matplotlib.pyplot as plt

def chord_area_equation(h, R, A):
    return R**2 * np.arccos(1 - h / R) - (R- h) * np.sqrt(R**2 - (R - h)**2) - A

R = 1
A = 0.16350110879328433
result = root(chord_area_equation, R/2, args=(R, A), tol=1E-18)
print(result)

x = np.linspace(0, 2, 101)
y = chord_area_equation(x, R, 0)
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title('Area under chord vs height\n' + r'$a = R^2 \arccos{\left ( 1 - \frac{h}{R} \right ) - (R- h)} \sqrt{R^2 - (R - h)^2}$')
plt.grid()