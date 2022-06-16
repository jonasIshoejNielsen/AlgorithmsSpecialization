from sys import stdin
import random
import numpy as np
import math
import cmath
import copy
from scipy.optimize import linprog
from itertools import chain, combinations
import scipy.special
from NicePathDecompostionOfGrid import Node, toPathDecomposition

def powerset(lst):
    #method for subsets: by https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset    #too lazy to do my own
    sets = chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))
    return sets

def index(n,i,j):
    return i*n + j

def vIsIllegal(v,s):
    for (i,j) in s:
        c=abs(i-v[0])+abs(j-v[1])
        if(c>1 or c==0):
            continue
        return True
    return False


def countIndpendentSets(n, node, storedPrev):
    if(node.parent==None):
        return storedPrev[str([])]
    if(len(node.bag)==0):   #leaf
        storedPrev[str([])]=1
    newCache={}
    if(len(node.bag)<len(node.parent.bag)):     #introduce
        v=node.parent.bag[0]
        for s in powerset(node.parent.bag):
            s=list(s)
            id=str(s)
            if(v not in s):
                newCache[id]=storedPrev[id]
            elif (vIsIllegal(v,s)):
                newCache[id]=0
            else:
                s.remove(v)
                newCache[id]=storedPrev[str(s)]  
    else:       #forget
        v=node.bag[-1]
        for s in powerset(node.parent.bag):
            s=list(s)
            id, idU=str(s), str(s+[v])
            newCache[id]=storedPrev[id] + storedPrev[idU]
    return countIndpendentSets(n,node.parent, newCache)




def maximumIndpendentSets(weights,n,node, storedPrev):
    if(node.parent==None):
        return storedPrev[str([])]
    if(len(node.bag)==0):   #leaf
        storedPrev[str([])]=0
    newCache={}
    if(len(node.bag)<len(node.parent.bag)):     #introduce
        v=node.parent.bag[0]
        for s in powerset(node.parent.bag):
            s=list(s)
            id=str([index(n,i,j) for (i,j) in s])
            if(v not in s):
                newCache[id]=storedPrev[id]
            elif (vIsIllegal(v,s)):
                newCache[id]=-math.inf
            else:
                s.remove(v)
                newCache[id]=weights[index(n,v[0],v[1])]+storedPrev[str([index(n,i,j) for (i,j) in s])]  
    else:       #forget
        v=node.bag[-1]
        for s in powerset(node.parent.bag):
            s=list(s)
            id, idU=str([index(n,i,j) for (i,j) in s]), str([index(n,i,j) for (i,j) in s+[v]])
            newCache[id]=max(storedPrev[id], storedPrev[idU])
    return maximumIndpendentSets(weights,node.parent, newCache)



for n in range(1,5):
    for m in range(n,5):
        n,m,node=toPathDecomposition(n,m)
        #weights=[1 for i in range(n*m)]
        #print((n,m), maximumIndpendentSets(weights,n,node,{}))
        print((n,m), countIndpendentSets(n,node,{}))
        print("")

for n in range(1,10000):
    n,n,node=toPathDecomposition(n,n)
    print((n,n), countIndpendentSets(n,node,{}))
