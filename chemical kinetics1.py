# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:09:14 2023

@author: hoshantm
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def dadt(t, y, k):
    a = y[0]
    return -k * a

a0 = 1.0
t0 = 0.0
tf = 10.0

t_span = (t0, tf)
t_eval = np.linspace(t0, tf, 100)
plt.figure(figsize=(5, 4))
for k in (1, 0.5, 0.1):
    result = solve_ivp(dadt, t_span, [a0], args=(k,), t_eval=t_eval, events=lambda t, y, k:  y[0] - 0.5 * a0)
    half_life_time = result.t_events[0][0]
    plt.plot(result.t, result.y[0], label=f'$k = {k}' + r'\> s^{-1}$, Half Life = ' + f'{half_life_time:0.3f} s')
    plt.ylim((0, a0))
    plt.xlim(t_span)
    plt.xticks(np.arange(t0, tf+1, 1.0))
    plt.yticks(np.arange(0, a0+0.1, 0.1))
    plt.grid()
    
plt.legend()
