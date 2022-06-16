from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import math
import copy
from itertools import chain, combinations

def randomGeneralGraph(n, MaxW):
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            graph[i][j]=random.randint(1,MaxW)
            graph[j][i]=graph[i][j]
    for i in range(n):
        graph[i][i]=0
    return graph

def printGraph(g):
    for i in g:
        print(i)

def powerset(lst):
    #method for subsets: by https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset    #too lazy to do my own
    sets = chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))
    sortedSets = [[] for i in range(len(lst)+1)]
    for s in sets:
        sortedSets[len(s)].append(s)
    return sortedSets[1:]

def toPath(cache, x, sub):
    if(len(sub)==0):
        return []
    (v,p)=cache[(x,str(sub))]
    sub.remove(p)
    lst=toPath(cache, p, sub)
    lst.append(p)
    return lst

def costPath(g, path):
    curr=path[0]
    sum=0
    for i in range(1,len(path)):
        sum+=g[curr][path[i]]
        curr=path[i]
    return sum

def DP_TSP(g):
    s=0
    allElements=[v for v in range(0,len(g))][1:]
    sortedSets = powerset(allElements)
    cache={}
    for sub in sortedSets[0]:
        cache[(sub[0],str([]))]=(g[sub[0]][s], s)
    for subs in sortedSets[1:]:
        for subPrime in subs:
            for e in subPrime:
                sub = list(subPrime)
                sub.remove(e)
                cache[(e,str(sub))]=cost(g, e, sub, cache)
    cache[(s,str(allElements))]=cost(g, s, allElements, cache)
    path=toPath(cache, s, allElements)
    path=[s]+path+[s]
    return costPath(g,path),path

def cost(g, e, sub, cache):
    bestV,bestX=math.inf, None
    for x in sub:
        #todo replace with sub.pop(x) and later sub.push(x)
        subCurr = copy.copy(sub)
        subCurr.remove(x)
        (v,_)=cache[(x, str(subCurr))]
        currVal=v+g[e][x]
        if(currVal<bestV):
            bestV,bestX = currVal, x
    return (bestV,bestX)


def main():
    n=4
    g=randomGeneralGraph(n, 100)
    #g=[[0, 84, 1, 72], [84, 0, 22, 50], [1, 22, 0, 1], [72, 50, 1, 0]]
    printGraph(g)
    v,path=DP_TSP(g)
    print("")
    print(v,path)


#main()