# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 08:04:50 2023

The Lorentz Attractor http://en.wikipedia.org/wiki/Lorenz_system

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def dydt(t, x, sigma, rho, beta):
    x, y, z = x[0], x[1], x[2]
    dxdt = sigma * ( y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return dxdt, dydt, dzdt

t0 = 0.0 
tf = 30.0
sigma = 10
rho = 28
beta = 8/3
x0 = 1
y0 = 1
z0 = 1

t_eval = np.linspace(t0, tf, 10000)

result = solve_ivp(dydt, (t0, tf), [x0, y0, z0], t_eval=t_eval, args=(sigma, rho, beta), method='Radau')

figsize = (10, 2)
plt.figure(figsize=figsize)
plt.plot(result.t, result.y[0])
plt.title('The Lorenz attractor - $x(t)$')
plt.figure(figsize=figsize)
plt.plot(result.y[0], result.y[1])
plt.title('The Lorenz attractor - $y(x)$')
plt.figure(figsize=figsize)
plt.plot(result.y[0], result.y[2])
plt.title('The Lorenz attractor - $z(x)$')
