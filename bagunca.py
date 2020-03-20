#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:50:51 2020

@author: erich

minimal
"""

import numpy as np #importante para os arrays do numpy
from matplotlib import pyplot as plt #importate para plotar

"""
exemplos de listas
"""
lista = ["asd",0,[1,2,3],3.2,2,4,1]
#pegar elemento de uma lista
lista[0]
lista[-1]
lista[0:3]
lista[1::]
lista[::3]
#tamanho da lista
len(lista)
print(lista)

a = np.zeros(3)

# array do numpy permite operação aritmetica
b = np.array([1,2,3,4,5])
np.size(b)

#numpy roll permite realizar deslocamentos
np.roll(b,1)
b
np.roll(b,-1)


#definindo uma rede de zeros
rede = np.zeros([5, 5])

#colocando elementos na rede
rede[3] = b
plt.imshow(rede)
# plt.imshow(rede, vmin = 0, vmax = 1, cmap = 'binary')


RuleKey60  = [0,0,1,1,1,1,0,0]

REGRA_EVOLUCAO(1,2,1,b)

def REGRA_EVOLUCAO(a,b,c,regra_usada):
    d = a+b+c - regra_usada[0]
    return d
