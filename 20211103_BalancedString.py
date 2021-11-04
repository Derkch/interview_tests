# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:41:40 2021

@author: alexd
"""

#La prueba consiste en responder si una cadena está balanceada.


def balance(string):
    
    #Primero descartamos casos limite:
    if string[0] in r")[A-z][0-9]+-_!?@":
        return False
    if sum(1 if char == "(" else -1 for char in string) == 0:
        return True
    else:
        return False
    

cad1 = "((()))(()(())(()((())))(())(())())()"
cad2 = "()()()("
cad3 = ")()()"
cad4 = "(((((((("
cad5 = "())))))))))))))"

print(balance(cad1))
print(balance(cad2))
print(balance(cad3))
print(balance(cad4))