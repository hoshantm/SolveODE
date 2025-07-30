# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:11:34 2023

@author: hoshantm
"""


from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Wikipedia Stiff Equation https://en.wikipedia.org/wiki/Stiff_equation
def wikipedia_stiff_dydt(t, y):
    # Differential equation: y' = -15y
    return -15*y

def wikipedia_stiff_exact_solution(t, y0):
    return np.exp(-15 * t)

def free_fall_dydt(t, y):
    # Differential equation: x'' = -g
    g = 9.81
    x, v = y # Get x and x' (x is not used to calculate anything and could thus be ignored)
    return v, -g # return x', x''

def free_fall_exact_solution(t, y0):
    g = 9.81
    return y0[0] + y0[1] * t - 1/2 * g * t**2 

# https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/17%3A_Second-Order_Differential_Equations/17.03%3A_Applications_of_Second-Order_Differential_Equations
def mass_spring_dydt(t, y):
    # Differential equation: mx'' + kx=0
    k = 4  # spring coefficient
    w = 2  # weight in lb
    g = 32 # f/s2
    m = w / g
    x, v = y[0], y[1] # y array contains x and x'
    a = -k / m * x    # calculate x''
    return v, a       # return x' and x''

def mass_spring_exact_solution(t, y0):
    return -2 * np.sin(8 * t)
    
def evaluate_methods(dydt, t_span, y0, title, f):
    methods = ['RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA']
    
    for method in methods:
        result = solve_ivp(dydt, t_span, y0, method=method)
        t = np.linspace(0, t_span[1], 1000)
        y_exact = f(t, y0)
        
        plt.figure()
        plt.scatter(result.t, result.y[0])
        plt.plot(t, y_exact)
        
        final_error_magnitude = np.log(np.abs(y_exact[-1] - result.y[0][-1]))
        plt.title(f'{title} - {method}\nFunction Calls = {result.nfev}, Final Error Magnitude = {final_error_magnitude:0.1f}')
        

evaluate_methods(wikipedia_stiff_dydt, (0, 1), [1], 'Wikipedia Stiff Equation', wikipedia_stiff_exact_solution)
evaluate_methods(free_fall_dydt, (0, 10), [0, 50], 'Free Fall', free_fall_exact_solution)
evaluate_methods(mass_spring_dydt, (0, 3), [0, -16], 'Mass Spring', mass_spring_exact_solution)