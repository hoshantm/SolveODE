#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:23:06 2024

@author: tarik
"""

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Wikipedia Stiff Equation https://en.wikipedia.org/wiki/Stiff_equation
# MATLAB https://es.mathworks.com/help/simulink/ug/model-a-differential-algebraic-equation.html
# https://scipython.com/book2/chapter-8-scipy/examples/solving-a-system-of-stiff-odes/

def wikipedia_stiff_dydt(t, y, total):
    a, b = y
    c = total - a - b
    a_dot = -0.04 * a + 1E4 * b * c
    b_dot = 0.04 * a - 1E4 * b * c - 3E7 * b**2
    dydt = np.array([a_dot, b_dot])    
    return dydt

tf = 1E6
t_span = (0.0, tf)
a0 = 1.0
b0 = 0.0
c0 = 0.0

total = a0 + b0 + c0

t_eval = np.linspace(0, tf, 10**6)

result = solve_ivp(wikipedia_stiff_dydt, t_span, [a0, b0], dense_output=True, args=(total,), method='LSODA')
t = np.linspace(0, t_span[1], 1000)

fig = plt.figure(figsize=(6, 10))
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.xscale('log')
plt.xlabel('Time')
ax1.plot(result.t, result.y[0], label='A', color='blue')
ax2.plot(result.t, result.y[1] * 10E4, label='B', color='green')
ax1.plot(result.t, 1 - result.y[0] - result.y[1], label='C', color='orange')
ax1.legend()
ax2.legend()
ax1.set_ylabel('A & C Concentrations')
ax2.set_ylabel('B Concentration')
ax1.set_xlabel('Time (s)')



