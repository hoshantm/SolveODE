# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:55:05 2023

@author: hoshantm
"""
import numpy as np

def sleeve_thickness(operating_pressure, pipe_diameter):
    epsilon_c = 0.25 / 100
    E_c = 3.9E6
    steel_modulus = 30E6
    t_s = 0
    thickness =  1 / (epsilon_c * E_c) * (2 * operating_pressure * pipe_diameter / 2 - steel_modulus * t_s) 
    thickness = thickness * 25.4
    return thickness


print(sleeve_thickness(100, 4))

from itertools import product

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

a = product(numbers, letters)
a = list(a)

x = np.linspace(1, 2, 6)
y = np.linspace(0.1, 0.25, 10)
z = np.linspace(100, 300, 5)

m = np.meshgrid(x, y, z)


