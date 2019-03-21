import collections as col
from collections import Counter



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


def euclidean_distance(x,y):
  
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
print euclidean_distance([0,3,4,5],[7,6,3,-1])

def manhattan_distance(x,y):
  
  return sum(abs(a-b) for a,b in zip(x,y))
  
print manhattan_distance([10,20,10],[10,20,20])

def nth_root(value, n_root):
  
 root_value = 1/float(n_root)
 return round (Decimal(value) ** Decimal(root_value),3)
  
def minkowski_distance(x,y,p_value):
  
 return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)
  
print minkowski_distance([0,3,4,5],[7,6,3,-1],3)

def square_rooted(x):
  
   return round(sqrt(sum([a*a for a in x])),3)
  
def cosine_similarity(x,y):
  
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),3)
  
print cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15])

def square_rooted(x):
  
   return round(sqrt(sum([a*a for a in x])),3)
  
def cosine_similarity(x,y):
  
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),3)
  
print cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15])


# Class

from math import*
from decimal import Decimal
  
class Similarity():
  
  """ Five similarity measures function """
  
  def euclidean_distance(self,x,y):
  
   """ return euclidean distance between two lists """
  
   return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
  def manhattan_distance(self,x,y):
  
   """ return manhattan distance between two lists """
  
   return sum(abs(a-b) for a,b in zip(x,y))
  
  def minkowski_distance(self,x,y,p_value):
  
   """ return minkowski distance between two lists """
  
   return self.nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)
  
  def nth_root(self,value, n_root):
  
   """ returns the n_root of an value """
  
   root_value = 1/float(n_root)
   return round (Decimal(value) ** Decimal(root_value),3)
  
  def cosine_similarity(self,x,y):
  
   """ return cosine similarity between two lists """
  
   numerator = sum(a*b for a,b in zip(x,y))
   denominator = self.square_rooted(x)*self.square_rooted(y)
   return round(numerator/float(denominator),3)
  
  def square_rooted(self,x):
  
   """ return 3 rounded square rooted value """
  
   return round(sqrt(sum([a*a for a in x])),3)
  
  def jaccard_similarity(self,x,y):
  
   """ returns the jaccard similarity between two lists """
  
   intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
   union_cardinality = len(set.union(*[set(x), set(y)]))
   return intersection_cardinality/float(union_cardinality)