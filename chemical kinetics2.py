# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:09:14 2023

@author: hoshantm
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def d_concentrations_dt(t, y, k):
    return -k[0] * y[0], k[0] * y[0] - k[1] * y[1], k[1] * y[1]

a0 = 1.0
b0 = 0.0 
c0 = 0.0


k1 = 0.1 
k2 = 0.5

t0 = 0.0
tf = 20.0

k = [k1, k2]
y0 = [a0, b0, c0]

t_span = (t0, tf)

t_eval = np.linspace(t0, tf, 100)
result = solve_ivp(d_concentrations_dt, t_span, y0, args=(k,), t_eval=t_eval)

labels=['A', 'B', 'C']
colors = ['red', 'green', 'blue']
plt.figure(figsize=(5, 4))
for i in range(3):
    plt.plot(result.t, result.y[i] / a0, label=f'[${labels[i]}]/[A]_0$', color=colors[i])
plt.ylim((0, a0))
plt.xlim(t_span)
plt.xticks(np.arange(t0, tf+1, 1.0))
plt.yticks(np.arange(0, a0+0.1, 0.1))
plt.legend()
plt.grid()

