from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import math


def randomGraph(n, A, edgeProp):
    B=2*A-1     #IF range [A,B] for 2A > B then triangleEquality holds
    randRange=1000
    edgeRange=float(randRange)*edgeProp
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            if(random.uniform(0,randRange)<=edgeRange):
                graph[i][j]=random.randint(A,B)
                graph[j][i]=graph[i][j]
    for i in range(n):
        graph[i][i]=0
    return graph

def path(explored, u, v):
    (cost, fromN,toN) = explored[v]
    if (fromN == u):
        return [(u,v)]
    res=path(explored, u, fromN)
    res.append((fromN, toN))
    return res

def cost(g, u,v):
    explored = {}
    frontier = []
    if(u==v):
        return (0,explored)
    for i in range(len(g[u])):
        if(g[u][i]>0):
            heappush(frontier, (g[u][i], u,i))
    while(frontier != []):
        (cost, fromN,toN) = heappop(frontier)
        if toN in explored:
            continue
        if v in explored:
            return (explored[v][0], explored)
        explored[toN] = (cost, fromN,toN)
        for i in range(len(g[toN])):
            if(g[toN][i]>0):
                heappush(frontier, (g[toN][i]+cost, toN,i))
    return (-1, explored)


def printGraph(g):
    for i in g:
        print(i)
def printCost(g,u,v):
    (val, explored)=cost(g,u,v)
    print("Cost:",u,v,"=",val)
    if(val>0):
        print('\t', path(explored, u, v))

g=randomGraph(5, 100, 1.0/2.0)
printGraph(g)


printCost(g,0,1)
printCost(g,0,2)
printCost(g,0,3)
printCost(g,0,4)