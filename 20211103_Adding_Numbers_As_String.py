# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:01:59 2021

@author: alexd
"""

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.


num1 = '364'
num2 = '1836'

def solution(num1,num2):
    return eval(num1 + " + " + num2)

print(solution(num1,num2))


# Output:
# 2200
# 2200

"""El truco aqui está en conocer la funcion eval() que esencialmente ejecuta texto como
    si estuviera escrito en consola.
    Ejemplo:
        In: eval("34 * 56")
        Out: 1904
"""