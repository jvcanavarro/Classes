
import numpy as np
import pandas as pd
import random
from collections import Counter
import math


inf=float(1e-20)
def rootX2(x):
    aux=0
    for i in range(len(x)):
	    aux += (x[i])**2
    return np.sqrt(aux) 


def cosine_similarity(x,y):
    return sum(a*b for a,b in zip(x,y))/(inf+float(rootX2(x)*rootX2(y)))

def euc_distance(x,y):
    aux=0;
    for i in range(len(x)):
        aux += (x[i]-y[i])**2
    return np.sqrt(aux)

def moda(s):
    lf=Counter(s).items()
    x=sorted(lf,key=lambda x: x[1])
    return x[-1][0]

def norma(x):
    aux=0
    for i in range(len(x)):
        aux += (x[i])**2
    return np.sqrt(aux) 

def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))
 
x=[6,1,3,2]
y=[3,1,1,4]
z=[6,2,2,8]
a=[1,2,1]
b=[3,1,2]
cd=[(1,2),(5,6), (11,3)]

print(list(zip(x, y)))
print(list(zip(a, b)))
c, d = zip(* cd)
print('cd:',c, d)

print('Distance X - Y:', euc_distance(x, y))
print('Distance Y - Z:', euc_distance(y, z))

print('Norma X:',norma(x))
print('Norma Y:',norma(y))

print('Moda X:',moda(x))
print('Moda Y:',moda(y))

print('Manhattan Distance X - Y:', manhattan_distance(x, y))
print('Manhattan Distance Y - Z:', manhattan_distance(x, z))

print('Euclidian Distance X - Y:', euc_distance(x, y))
print('Euclidian Distance Y - Z:', euc_distance(y, z))

print('Cosine Distance X - Y:', cosine_similarity(x, y))
print('Cosine Distance Y - Z:', cosine_similarity(y, z))

