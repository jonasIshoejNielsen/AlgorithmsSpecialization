from sys import stdin
import math
import random
import numpy as np
from scipy.optimize import linprog


def randomInstance(max_n, maxF):
    universe=[i for i in range(random.randint(1,max_n))]
    k=random.randint(1, len(universe))
    sets=[[] for i in range(k)]
    for v in universe:
        sets[random.randint(0,k-1)].append(v)
        for i in range(random.randint(0,maxF-1)):
            if(i<2):
                continue    #to make less copies
            currSet=sets[random.randint(0,k-1)]
            if(v not in currSet):
                currSet.append(v)
    c=lambda S: len(S)
    return (universe, sets, c)

def a(S, C, c):
    count=0
    for s in S:
        if (s not in C):
            count+=1
    if (count==0):
        return math.inf
    return c(S)/count

def SetCoverApproximation(universe, sets, c):
    C=[]
    selectedSets=[]
    while(len(C)!=len(universe)):
        best=[]
        minA=math.inf
        for s in sets:
            currA=a(s, C, c)
            if (currA < minA):
                minA=currA
                best=s
        for s in best:
            if (s not in C):
                C.append(s)
        selectedSets.append(best)
    return (C, selectedSets)


def arrayIfNotNone(ar):
    if(ar is None or len(ar)==0):
        return None
    return np.array(ar)

def runLP(c, isMinimize, A_ub=None, b_ub=None, A_eq=None, b_eq=None):
    return linprog(np.array(c) if isMinimize else -np.array(c), A_ub=arrayIfNotNone(A_ub), b_ub=arrayIfNotNone(b_ub), A_eq=arrayIfNotNone(A_eq), b_eq=arrayIfNotNone(b_eq))


def LP_Set_cover(universe, sets, cost, f):
    isMinimize=True
    c=[cost(s) for s in sets]     #since no weights, otherwise w(i) instead of 1
    A_ub=[]
    b_ub=[]
    for u in universe:
        A_curr=[0 - (u in s) for s in sets]
        A_ub.append(A_curr)
        b_ub.append(-1)

    xs=runLP(c, isMinimize, A_ub=A_ub, b_ub=b_ub)["x"]
    setsCovered=[]
    for i in range(len(sets)):
        if(xs[i]>=1.0/f):
            setsCovered.append(sets[i])
    return len(setsCovered), setsCovered, xs




maxF=5
(universe, sets, c) = randomInstance(100,5)
print("universe=",universe)
print("sets=",sets)
print("c=",c)
(res, selectedSets) = SetCoverApproximation(universe, sets, c)
res.sort(key=lambda e: e)
print("")
print("covered elements=",len(res), " universe=",len(universe))
selectedSets.sort(key=lambda e: e)
print("selectedSets")
print(len(selectedSets), selectedSets)

print("")
print("LP_Set_cover")
count, vertices, xs=LP_Set_cover(universe, sets, c, maxF)
print(count, vertices)


