# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:06:50 2023

https://en.wikipedia.org/wiki/Van_der_Pol_oscillator

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def dydt(t, x, mu):
    x, y = x[0], x[1]
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return dxdt, dydt

t0 = 0.0 
tf = 30.0
x0 = -2
y0 = 0
mu = 1
t_eval = np.linspace(t0, tf, 1000)

result = solve_ivp(dydt, (t0, tf), [x0, y0], t_eval=t_eval, args=(mu,), method='Radau')

plt.figure()
plt.plot(result.t, result.y[0])
plt.title('Van Der Pol Oscillator - $x(t)$')
plt.grid()
plt.figure()
plt.plot(result.t, result.y[1])
plt.title('Van Der Pol Oscillator - $y(t)$')
plt.grid()
