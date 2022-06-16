import math
from sys import stdin
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def getRandomCNF(maxN, maxM, minL, maxL):
    n=random.randint(1,maxN)
    clauses=[]
    numberOfAssignments=0
    l=math.inf
    for i in range(random.randint(1, maxM)):
        current=[]
        for v in range(random.randint(minL, maxL)):
            current.append((random.randint(0,n-1),random.randint(0,100000)%2==0))
        clauses.append(current)
        l=min(len(current),l)
    return (clauses,n,l)

def isSatisfied(clauses, a):
    for c in clauses:
        worked=False
        for (i,neg) in c:
            if(a[i]==neg):
                worked=True
                break
        if(not(worked)):
            return c
    return None


def solve_k_SAT(clauses,n, printing=True):
    a=[random.randint(0,100000)%2==0 for v in range(n)]
    if(printing):
        print("solve_k_SAT")
    for i in range(0,3*n):
        if(printing):
            print('\t',"step:",i,"=",[(i,v) for (i,v) in enumerate(a)])
        c=isSatisfied(clauses,a)
        if(c is None):
            return (True,a)
        bitToSwitch=c[random.randint(0, len(c)-1)][0]
        a[bitToSwitch]=not(a[bitToSwitch])
    return (False, a)

def printClauses(clauses):
    print("clauses", len(clauses))
    for c in clauses:
        print('\t',c)


printing=True
maxN,maxM,minL,maxL = 20, 40, 3,3       #n=variables, m=cluses, l=frequency of each variable
(clauses,n,l)=getRandomCNF(maxN, maxM, minL, maxL)
if(printing):
    printClauses(clauses)
(success,a) =solve_k_SAT(clauses,n, printing=printing)
print("(success,a)")
print(success, [(i,v) for (i,v) in enumerate(a)])

