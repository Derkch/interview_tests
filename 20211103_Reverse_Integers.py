# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:05:34 2021

@author: alexd
"""

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(x):
    string = str(x)
    
    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])
    
print(solution(-231))
print(solution(345))

"""Explicacion:
    
    en listas o cadenas se puede utilizar el operador de iteracion [inicio:fin:paso].
    
    cuando se omite el inicio se empezará por el primer elemento, y cuando se omite el fin
    se terminara en el ultimo. Si el paso es negativo el inicio sera el ultimo elemento y el fin
    el primer elemento de la cadena/lista. ::-1 es un truco para invertir cadenas/listas.
    
    """