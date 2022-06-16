from sys import stdin
import random
import numpy as np
import math
import copy
from scipy.optimize import linprog


def randomGraph(n, maxScore):
    res=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            res[i][j]=random.randint(1, maxScore) if (random.uniform(0,1)>0.4) else None
            res[j][i]=res[i][j]
    for i in range(n):
        res[i][i]=None
    return res

def arrayIfNotNone(ar):
    if(ar is None or len(ar)==0):
        return None
    return np.array(ar)

def runLP(c, isMinimize, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=(0,None)):
    return linprog(np.array(c) if isMinimize else -np.array(c), A_ub=arrayIfNotNone(A_ub), b_ub=arrayIfNotNone(b_ub), A_eq=arrayIfNotNone(A_eq), b_eq=arrayIfNotNone(b_eq), bounds=bounds)

def removeNone(lst):
    return list(filter(lambda a: a is not None, lst))

def LP_Maximum_weight_matching(g):
    n=len(g)
    indexes=[[ (i,j) if g[i][j] is not None else None for j in range(i+1,n)] for i in range(n)]
    indexes = flatten(indexes)
    indexes = removeNone(indexes)

    c=[g[i][j] for (i,j) in indexes]
    A_eq, b_eq=[],[]
    for v in range(int(n/2.0)):
        A_curr=[-1 if i==v or j==v else 0 for (i,j) in indexes]
        A_eq.append(A_curr)
        b_eq.append(-1)
    xs=runLP(c, isMinimize=False, A_eq=A_eq, b_eq=b_eq, bounds=(0,1))["x"]
    g_xs=transform_LP_TO_ILP(xs,n, indexes)
    return xs,g_xs

def printGraph(g):
    for v in g:
        print(v)

def flatten(lst):
    return [item for sublist in lst for item in sublist]

#Transformation
def toIntIfNeeded(v):
    return [v,v==1 or v==0]

def xsToGraph(xs, n, indexes):
    g_xs=[[[0,True] for i in range(n)] for j in range(n)]
    for i in range(len(xs)):
        (u,v)=indexes[i]
        g_xs[u][v]=toIntIfNeeded(xs[i]) if round else xs[i]
        g_xs[v][u]=g_xs[u][v]
    return g_xs
def g_xsToNormalGraph(g_xs,n):
    return [[v[0] for v in row] for row in g_xs]

def findNonIntEdgeFrom(g_xs,n, i, notJ):
    for j in range(0, n):
        if(i==j or j==notJ or g_xs[i][j][1]):
            continue
        return j
    return None

def findNonIntEdge(g_xs,n):
    for i in range(n):
        e=findNonIntEdgeFrom(g_xs,n,i,-1)
        if(e is not None):
            return (i,e)
    return None

def findCycle(g_xs,n):
    e1=findNonIntEdge(g_xs, n)
    if(e1 is None):
        return None
    visited={}
    (a,b)=e1
    visited[a]=b
    visited[b]=a
    while(True):
        oldB=b
        b=findNonIntEdgeFrom(g_xs, n, oldB, a)
        if(b is None):
            #print("floating point error, remove edge: ", a,oldB)
            g_xs[a][oldB]=[round(g_xs[a][oldB][0]), True]
            g_xs[oldB][a]=g_xs[a][oldB]
            return findCycle(g_xs, n)   #todo
        if(b in visited):
            visited[b]=oldB
            break
        visited[b]=oldB
        a=oldB
    return visited, b

def relaxEdges(g_xs,n, visited, b):
    curr=b
    bestEpsilon,isEven=math.inf,True
    currEven=True
    next=None
    while(next != b):
        next=visited[curr]
        currV=g_xs[curr][next][0]
        if(currV>1-g_xs[curr][next][0]):
            currV=-(1-g_xs[curr][next][0])
        if (abs(currV) < abs(bestEpsilon)):
           bestEpsilon=currV
           isEven=currEven
           #print("update at", curr, next,g_xs[curr][next][0], currV)
        currEven=not(currEven)
        curr=next
    if (not(isEven)):
        bestEpsilon=-bestEpsilon
    #print("bestEpsilon",bestEpsilon, isEven)
    curr=b
    next=None
    currEven=True
    while(next != b):
        next=visited[curr]
        old=g_xs[curr][next][0]
        g_xs[curr][next][0]+= -bestEpsilon if currEven else bestEpsilon
        g_xs[curr][next]=toIntIfNeeded(g_xs[curr][next][0])
        #print('\t',curr,next,currEven, old, "+" + ("-"+str(bestEpsilon)) if currEven else str(bestEpsilon), g_xs[curr][next][0])
        g_xs[next][curr]=g_xs[curr][next]
        currEven=not(currEven)
        curr=next

def transform_LP_TO_ILP(xs,n, indexes):
    g_xs=xsToGraph(xs,n, indexes)
    cycle = findCycle(g_xs,n)
    while(cycle is not None):
        visited, b = cycle
        relaxEdges(g_xs, n, visited, b)
        cycle = findCycle(g_xs,n)
    return g_xsToNormalGraph(g_xs,n)

for i in range(100):
    n=6
    g=randomGraph(n, 100)   #bipartite graph
    #g=[[0, 0, 0, 47, None, 86], [0, 0, 0, None, 54, None], [0, 0, 0, 43, None, None], [47, None, 43, 0, 0, 0], [None, 54, None, 0, 0, 0], [86, None, None, 0, 0, 0]]

    #g=[[0, 0, 0, 25, 37, 76], [0, 0, 0, 79, 38, 57], [0, 0, 0, 36, 91, 65], [25, 79, 36, 0, 0, 0], [37, 38, 91, 0, 0, 0], [76, 57, 65, 0, 0, 0]]
    
    xs,g_xs=LP_Maximum_weight_matching(g)
    if(max(xs)==0.0):
        continue
    print(max(xs))
    #"""
    print("g:")
    printGraph(g)

    print("g_xS:")
    printGraph(g_xs)
    break
    #"""



##note floating points error causes print("floating point error, remove edge: ", a,oldB)
##Note max(xs) can be above 1 because of the LP solver isn't accurate