# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 07:51:47 2023

@author: hoshantm
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

pde_def = 'Wave Equation\n' + r'$\frac{\partial^2u}{\partial t}=a^2\frac{\partial^2u}{\partial x^2}$' + '\n' + r'$u(t=0, x) = a^2 sech(x)$' + '\n' + r'$\frac{\partial u}{\partial t}_{(t=0)} = 0$'
        
#RHS of equations
def f(t, u, a, deltax):
    N = len(u) // 2
    uxx = np.gradient(np.gradient(u[:N], deltax), deltax)
    du1dt=u[N:]
    du2dt =a**2 * uxx
    dudt=np.append(du1dt, du2dt)
    return dudt

a=1
amin=-40; bmax=40
N=1000
assert N % 2 == 0
deltax = (bmax - amin) / (N - 1)
x = np.linspace(amin, bmax, N)
t_eval = [0, 5, 10, 20]

u01 = 2*np.cosh(x)**(-1)
u02 = np.zeros(N)
# y0
inital=np.append(u01, u02)

sola1 = solve_ivp(f, t_span=[0, 40], t_eval=t_eval, y0=inital, args=(a, deltax))

for i in range(len(sola1.t)):
    fig, ax = plt.subplots(figsize=(20, 4))
    ax.plot(x,sola1.y[:N, i])
    plt.title(f'{pde_def}\na = {a}\nSolution at t = {sola1.t[i]}', fontsize=30)
    plt.ylim([0, 2])