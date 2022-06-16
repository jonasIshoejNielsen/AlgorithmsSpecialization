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

def delete(g,v):
    n=len(g)
    newG=[[g[j][i] for i in range(n)] for j in range(n)]
    for i in range(n):
        newG[i][v]=0
        newG[v][i]=newG[i][v]
    return newG

def rule1(g,k):
    for i in range(len(g)):
        if sum(g[i])<=1:
            print("r1, delete",i)
            return(delete(g, i),k)
    return (g,k)

def rule2(g,k):
    for i in range(len(g)):
        if sum(g[i])>=k+1:
            print("r2, delete",i)
            return(delete(g, i),k-1)
    return (g,k)

def getKernel(g,k):
    prevN=len(g)
    while(True):
        g,k=rule1(g,k)
        g,k=rule2(g,k)
        if(prevN==len(g)):
            break
        prevN=len(g)
    
    return g,k


def printG(g):
    print("graph")
    for v in g:
        print('\t',v)


g=randomGraph(5)
k=random.randint(0, len(g))
print(k)
printG(g)
g,k=getKernel(g,k)
print(k)
printG(g)