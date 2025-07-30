# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:22:31 2023

https://en.wikipedia.org/wiki/Three-body_problem

@author: hoshantm
"""
from scipy.integrate import solve_ivp
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def dxdt(t, x, G, m1, m2, m3):
    r1 = x[0:3]
    r2 = x[3:6]
    r3 = x[6:9]    
    r1dotdot = -G * m2 * (r1 - r2) / norm(r1 - r2)**3 - G * m3 * (r1 - r3) / norm(r1 - r3)**3
    r2dotdot = -G * m3 * (r2 - r3) / norm(r2 - r3)**3 - G * m1 * (r2 - r1) / norm(r2 - r1)**3 
    r3dotdot = -G * m1 * (r3 - r1) / norm(r3 - r1)**3 - G * m2 * (r3 - r2) / norm(r3 - r2)**3
    f = np.full(18, np.nan)
    f[0:9] = x[9:18] # r1dot, r2dot, r3dot
    f[9:12] = r1dotdot
    f[12:15] = r2dotdot
    f[15:18] = r3dotdot
    return f

r1 = np.empty(3)
v1 = np.empty(3)
r1[0] = -10
r1[1] = 10
r1[2] = -11
v1[0] = -3
v1[1] = 0
v1[2] = 0

r2 = np.empty(3)
v2 = np.empty(3)
r2[0] = 0 
r2[1] = 0
r2[2] = 0 
v2[0] = 0
v2[1] = 0
v2[2] = 0

r3 = np.empty(3)
v3 = np.empty(3)
r3[0] = 10
r3[1] = 10
r3[2] = 12
v3[0] = 3
v3[1] = 0
v3[2] = 0

x0 = np.empty(18)
x0[0:3] = r1
x0[3:6] = r2
x0[6:9] = r3
x0[9:12] = v1
x0[12:15] = v2
x0[15:18] = v3
 
t0 = 0 
tf = 200
delta_t = 0.001
t_eval = np.linspace(t0, tf, int((tf - t0) / delta_t))
m1 = 10
m2 = 20
m3 = 30
G = 9.8

methods = methods = ['RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA']

plots = {}

for method in methods:
    print(f'Computing using {method}...')
    result = solve_ivp(dxdt, (t0, tf), x0, args=(G, m1, m2, m3), t_eval=t_eval, method=method, atol=1E-8, rtol=1E-8)
    
    print(f'Preparing plot for {method}...')   
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d')
    fig.gca().patch.set_facecolor('black')
    
    y = result.y
    plt.plot(y[0], y[1], y[2], '^', color='red', lw=0.05, markersize=0.01, alpha=0.5)
    plt.plot(y[3], y[4], y[5], '^', color='white', lw=0.05, markersize=0.01, alpha=0.5)
    plt.plot(y[6], y[7], y[8], '^', color='blue', lw=0.05, markersize=0.01, alpha=0.5)
    plt.axis('on')
    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
    plt.title(f'Three Body Problem\nSolver = {method}')

    plots[method] = fig
    
while True:
    print('Select Method to be displayed:')
    for i, method in enumerate(methods):
        print(f'{i+1} {method}')
    print('Any other input to exit.')
    
    try:
        selected = int(input('Method number: '))
    except:
        break
    
    if 1 <= selected <= len(methods):
        selected -= 1
        plots[methods[selected]].show()
    else:
        break

