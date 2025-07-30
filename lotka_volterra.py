#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:20:10 2024

@author: Hoshan, Tarik M (hoshantm@gmail.com)

Lotka-Volterra equations - https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations

"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def lotka_volterra(x0, y0, t0, tf, alpha, beta, gamma, delta):
    def dydt(t, x, alpha, beta, gamma, delta):
        x, y = x[0], x[1]
        dxdt = alpha * x - beta * x * y
        dydt = -gamma * y + delta * x * y
        return dxdt, dydt

    t_eval = np.linspace(t0, tf, 1000)
    result = solve_ivp(dydt, (t0, tf), [x0, y0], t_eval=t_eval, args=(alpha, beta, gamma, delta), method='Radau')
    return result

t0 = 0.0 
tf = 100.0
x0 = 10.0
y0 = 10.0
alpha = 1.1
beta = 0.4
gamma = 0.4
delta = 0.1

result = lotka_volterra(x0, y0, t0, tf, alpha, beta, gamma, delta)

plt.figure(figsize=(10, 6))
plt.plot(result.t, result.y[0], label='x')
plt.plot(result.t, result.y[1], label='y')
plt.title('Lotka-Volterra')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')

plt.figure(figsize=(10, 10))
plt.title('Lotka-Volterra')
for y0 in [1, 2, 5, 7, 10, 12, 15]:
    result = lotka_volterra(x0, y0, t0, tf, alpha, beta, gamma, delta)
    plt.plot(result.y[0], result.y[1], label=f'y0 = {y0}')
    plt.title('Lotka-Volterra')
    plt.xlabel('x population')
    plt.ylabel('y population')
    
