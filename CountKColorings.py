from sys import stdin
import random
import numpy as np
import math
import cmath
import copy
from scipy.optimize import linprog
from itertools import chain, combinations
import scipy.special

def randomGraph(n):
    res=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            res[i][j]=random.randint(0, 1)
            res[j][i]=res[i][j]
    for i in range(n):
        res[i][i]=0
    return res

def contains(v, s):
    for k in s:
        if (k==v):
            return True
    return False

def addNeighbors(g,v,s):
    for i in range(len(g)):
        if(g[i][v]==0):
            continue
        if(contains(i,s)):
            continue
        s.append(i)
    return s


def AmmountOfNonEmptyIndependentSubsets(g,s, DPCache):
    s.sort()
    if (str(s) in DPCache):
        return DPCache[str(s)]
    if(len(g)-len(s)==0):
        DPCache[str(s)]=0
        return DPCache[str(s)]
    for v in range(len(g)):
        if (not(contains(v,s))):
            break
    #print(v, v not in s,contains(v,s), s)
    sCopy1,sCopy2 = copy.copy(s),copy.copy(s)
    sCopy1.append(v)
    sCopy2.append(v)
    sCopy2=addNeighbors(g,v,sCopy2)
    res = AmmountOfNonEmptyIndependentSubsets(g,sCopy1, DPCache)+AmmountOfNonEmptyIndependentSubsets(g,sCopy2, DPCache)+1
    DPCache[str(s)]=res
    return res


def valueOfSubset(g,k, s, DPCache):
    lastPart=math.pow(AmmountOfNonEmptyIndependentSubsets(g,s, DPCache), k)
    #print(s, math.pow(-1,len(g)-len(s))*lastPart)
    return math.pow(-1,len(g)-len(s))*lastPart

def powerset(lst):
    #method for subsets: by https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset    #too lazy to do my own
    sets = chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))
    return sets


#inclusion exclusion
def CountKColorints(g,k):
    sets=powerset([v for v in range(len(g))])
    count=0
    DPCache={}
    for s in sets:
        count+=valueOfSubset(g,k,list(s),DPCache)
    #print(DPCache)
    return round(count) #to make smarter
"""
def main():
    for i in range(1):
        n=4
        g=randomGraph(n)
        for v in g:
            print(v)
        for k in range(n):
            res=CountKColorints(g,k)
            print("k=",k)
            print(res)
            print("")
        
main()
"""
g=randomGraph(4)    
for v in g:
    print(v)
for k in range(len(g)):
    print("k=",k)
    res=CountKColorints(g,k)

    print(res)
    print("")
