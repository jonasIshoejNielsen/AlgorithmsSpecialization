from sys import stdin
import random
import numpy as np
import math
import cmath
import copy
import itertools
from scipy.optimize import linprog
import scipy.special

def subsetOfLength(k, lst):
    return list(itertools.combinations(lst, k))

def atMost(k, literals):
    clauses=[]
    for lit in subsetOfLength(k+1, literals):
        clauses.append([(v*-1) for v in lit])
    return clauses

def atLeast(k, literals):
    return [list(v) for v in subsetOfLength(len(literals)-k+1, literals)]

def exactly(k, literals):
    return atMost(k, literals) + atLeast(k, literals)

def getNeighbors(v,g):
    res=[]
    for i in range(len(g)):
        if(g[v][i]>0):
            res.append(i)
    return res

def ReduceHamiltonianCycle(g):
    n=len(g)
    variables=[]
    for i in range(n):
        for j in range(i+1, n):
            variables.append((i,j))
    indexes={}
    for (i,val) in enumerate(variables):
        indexes[val]=i+1
        
    clauses = []
    for v in range(n):
        neighbors=getNeighbors(v,g)
        literals=[indexes[min(v,j), max(v,j)] for j in neighbors]
        clauses+=exactly(2, literals)
    clauses+=exactly(n, [indexes[v] for v in variables])
    return variables, clauses


def printSAT(variables, clauses):
    print("p cnf "+str(len(variables))+" "+str(len(clauses)))
    for c in clauses:
        val=""
        for v in c:
            val+=str(v) +" "
        print(val+"0")


g=[ [0,1,1],
    [1,0,1],
    [1,1,0]]
g=[ [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]]


variables, clauses= ReduceHamiltonianCycle(g)
print("variables:")
print([(i+1,v) for (i,v) in enumerate(variables)])
print("")
print("https://jgalenson.github.io/research.js/demos/minisat.html")
print("")
printSAT(variables, clauses)