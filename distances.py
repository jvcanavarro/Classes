import collections as col
from collections import Counter
s=[1,2,3,4,1,2,3,3,1,2,3,4,5]
print(Counter(s).values())
print(Counter(s).keys())
print(Counter(s).items())
'''ss=Counter(s)
print(ss.items())
dict_items([(1, 3), (2, 3), (3, 4), (4, 2), (5, 1)])
'''
def moda(s):
    lf=Counter(s).items()
    x=sorted(lf,key=lambda x: x[1])
    return x[-1][0]

import random
list = [20,40,80,100,120]
print (random.sample(list,k=5))
print (random.sample(list,k=5))
exit(1)

### medidas de distancia e similaridade em vetores
'''
def euclD(x,y):return round(sqrt(sum(pow(a-b,2) for a, b in zip(x, y))),2)
def manhD(x,y):return round(sum(abs(a-b) for a,b in zip(x,y)),2)
def rootX2( x ):return round(sqrt(sum([a*a for a in x])),2)  
def cosiV(x,y):return round(sum(a*b for a,b in zip(x,y))/(inf+float(rootX2(x)*rootX2(y))),2)
'''
from math import*
inf=float(1e-20)
def euclD(x,y):
    aux=0;
    for i in range(len(x)):
        aux += (x[i]-y[i])**2
    return sqrt(aux) 
def rootX2(x):
    aux=0;
    for i in range(len(x)):
        aux += (x[i])**2
    return sqrt(aux) 
def cosV(x,y):
    aux=0;
    for i in range(len(x)):
        aux += (x[i]*y[i])
    return aux/(inf+float(rootX2(x)*rootX2(y))) 

