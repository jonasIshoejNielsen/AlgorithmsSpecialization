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

def AmmountOfClosedWalks(g,s):
    n=len(g)
    if(n-len(s)==0):
        return 0
    GWithoutS=[[0 for v in range(n-len(s))] for v in range(n-len(s))]
    iCurr=0
    for i in range(n):
        if(i in s):
            continue
        jCurr=iCurr+1
        for j in range(i+1,n):
            if(j in s):
                continue
            GWithoutS[iCurr][jCurr]=g[i][j]
            GWithoutS[jCurr][iCurr]=GWithoutS[iCurr][jCurr]
            jCurr+=1
        iCurr+=1
    pow=np.linalg.matrix_power(np.array(GWithoutS), n)
    sum=0
    for i in range(len(pow)):
        sum+=pow[i][i]
    return sum


def valueOfSubset(g, s):
    return math.pow(-1,len(s))*AmmountOfClosedWalks(g,s) 


def powerset(lst):
    #method for subsets: by https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset    #too lazy to do my own
    sets = chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))
    return sets

def paritionOnSize(maxLenght, sets):
    sortedSets = [[] for i in range(maxLenght+1)]
    for s in sets:
        sortedSets[len(s)].append(s)
    return sortedSets[1:]

#inclusion exclusion
def CountHamiltonianCycles(g):
    sets=powerset([v for v in range(len(g))])
    count=0
    for s in sets:
        count+=valueOfSubset(g,s)
    return round(count) #to make smarter


#DP
def DPCountHamiltonianCycles(g):
    s=0
    allElements=[v for v in range(0,len(g))][1:]
    sortedSets = paritionOnSize(len(allElements), powerset(allElements))
    cache={}
    for sub in sortedSets[0]:
        cache[(sub[0],str([]))]=g[sub[0]][s]    #0 if no edge else 1
    for subs in sortedSets[1:]:
        for subPrime in subs:
            for e in subPrime:
                sub = list(subPrime)
                sub.remove(e)
                cache[(e,str(sub))]=cost(g, e, sub, cache)
            
    cache[(s,str(allElements))]=cost(g, s, allElements, cache)
    return cache[(s,str(allElements))]*len(g)


def cost(g, e, sub, cache):
    res=0
    for x in sub:
        #todo replace with sub.pop(x) and later sub.push(x)
        subCurr = copy.copy(sub)
        subCurr.remove(x)
        v=cache[(x, str(subCurr))]
        currVal=v*g[e][x]
        res+=currVal
    return res



#testing

def testEqualOnRandom(n, tests):
    for i in range(tests):
        g=randomGraph(n)
        res1=CountHamiltonianCycles(g)
        res2=DPCountHamiltonianCycles(g)
        if (res1!=res2):
            for v in g:
                print(v)
            print(res)
            return False
    return True



"""
for i in range(2, 7):
    print(i, testEqualOnRandom(i, 100))
"""

"""
for i in range(2, 17):
    g=randomGraph(i)
    res=CountHamiltonianCycles(g)
    print(i,res)
"""

"""
for i in range(2, 19):
    g=randomGraph(i)
    res=DPCountHamiltonianCycles(g)
    print(i,res)
"""