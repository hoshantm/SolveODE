# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:05:30 2023

@author: hoshantm
"""

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def decay_dydt(t, y, a, b):
    # Differential equation: y' = -a * y + b
    return -a * y + b

def decay_analytic(t, y0, a, b):
    return b / a + (y0 - b / a) * np.exp(-a * t)


t_span = (0, 10)

# Initial values
y0 = [5]
a = 1
b = 2

result = solve_ivp(decay_dydt, t_span, y0, args=(a, b))
t = np.linspace(0, t_span[1], 1000)
y_exact = decay_analytic(t, y0[0], a, b)

plt.figure()
plt.scatter(result.t, result.y[0])
plt.plot(t, y_exact)

final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[0][-1]))
plt.title(f'Decay - Wikipedia\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')
