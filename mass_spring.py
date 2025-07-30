# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:13:16 2023

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/17%3A_Second-Order_Differential_Equations/17.03%3A_Applications_of_Second-Order_Differential_Equations
def mass_spring_dydt(t, y):
    # Differential equation: mx'' + kx=0
    k = 4  # spring coefficient in N/m
    m = 0.0625 # kg
    x, v = y[0], y[1] # y array contains x and x'
    a = -k / m * x    # calculate x''
    return v, a       # return x' and x''

def mass_spring_analytical(t, y0):
    return -2 * np.sin(8 * t)
    

t_span = (0, 3)
y0 = [0, -16]
result = solve_ivp(mass_spring_dydt, t_span, y0)
t = np.linspace(0, t_span[1], 1000)
y_exact = mass_spring_analytical(t, y0)

plt.figure()
plt.scatter(result.t, result.y[0])
plt.plot(t, y_exact)

final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[0][-1]))
plt.title(f'Mass - Spring\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')
        

