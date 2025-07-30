# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:47:52 2023

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Wikipedia Stiff Equation https://en.wikipedia.org/wiki/Stiff_equation
def wikipedia_stiff_dydt(t, y):
    # Differential equation: y' = -15y
    return -15*y

def wikipedia_stiff_exact_solution(t, y0):
    return np.exp(-15 * t)


t_span = (0, 1)
y0 = [1]

result = solve_ivp(wikipedia_stiff_dydt, t_span, y0)
t = np.linspace(0, t_span[1], 1000)
y_exact = wikipedia_stiff_exact_solution(t, y0)

plt.figure()
plt.scatter(result.t, result.y[0])
plt.plot(t, y_exact)

final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[0][-1]))
plt.title(f'Stiff - Wikipedia\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')
