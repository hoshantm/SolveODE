# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:52:45 2023

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def projectile_dydt(t, y, vx0):
    # Differential equations: x' = vx0, y'' = -g
    g = 9.81
    x, y, dy = y # Get x, y and y' (y is not used to calculate anything and could thus be ignored)
    return vx0, dy, -g # return x', y' and y''

def projectile_exact_solution(t, y0, vx0):
    g = 9.81
    return vx0 * t, y0[1] + y0[2] * t - 1/2 * g * t**2 


t_span = (0, 10)
y0 = (0, 0, 50)

qq = np.linspace(0, t_span[1], 101)

vx0=30
result = solve_ivp(projectile_dydt, t_span, y0, args=(vx0,), t_eval=qq)
t = np.linspace(0, t_span[1], 1000)
x_exact, y_exact = projectile_exact_solution(t, y0, vx0)

plt.figure()
plt.plot(result.t, result.y[1])
plt.plot(t, y_exact)
plt.xlabel('t (s)')
plt.ylabel('y (m)')

final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[1][-1]))
plt.title(f'Projectile\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')

plt.figure()
plt.scatter(result.y[0], result.y[1])
plt.plot(x_exact, y_exact)
plt.xlabel('x (m)')
plt.ylabel('y (m)')

final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[1][-1]))
plt.title(f'Projectile\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')
