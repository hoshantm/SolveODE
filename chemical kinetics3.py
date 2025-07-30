# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:09:14 2023

@author: hoshantm
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def d_concentrations_dt(t, y, k):
    if t >= 0:
        dadt = k[1] * y[1] - k[0] * y[0]
    else:
        dadt = 0
    dbdt = -dadt
    return dadt, dbdt

a0 = 0.1
b0 = 0.2 

k1 = 0.1 
k2 = 0.2

t0 = -2.0
tf = 16.0

k = [k1, k2]
y0 = [a0, b0]

t_span = (t0, tf)

t_eval = np.linspace(t0, tf, 1000)
result = solve_ivp(d_concentrations_dt, t_span, y0, args=(k,), t_eval=t_eval, method='Radau')

labels=['A', 'B']
colors = ['red', 'green']
plt.figure(figsize=(5, 4))
for i in range(2):
    plt.plot(result.t, result.y[i], label=f'[${labels[i]}]$', color=colors[i])
plt.ylim((0, a0+b0))
plt.xlim(t_span)
plt.xticks(np.arange(t0, tf+2, 2.0))
plt.yticks(np.arange(0, (a0+b0) * 1.1, 0.05))
plt.legend()
plt.grid()

