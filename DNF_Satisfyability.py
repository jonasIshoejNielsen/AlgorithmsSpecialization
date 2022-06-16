import math
from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def getRandomDNF():
    t=random.randint(2,5)
    n=random.randint(t,10)
    clauses=[]
    numberOfAssignments=0
    for i in range(t):
        current=[]
        k2=random.randint(1,n)
        Si=math.pow(2,n-k2)
        for v in range(k2):
            current.append((random.randint(1,n),random.randint(0,100000)%2==0))
        numberOfAssignments+=Si
        clauses.append((current, Si))
    return (clauses,n,t,numberOfAssignments)

def sampleRandom(dnf,n,t,numberOfAssignments):
    i=0
    target=random.randint(0,numberOfAssignments)
    current=0
    for (clause,si) in dnf:
        current+=si
        if(current>=target):
            break
        i+=1
    (clause,_)=dnf[i]
    assignment=[random.randint(0,100000)%2==0 for v in range(n)]
    for (v,b) in clause:
        assignment[v-1]=b
    return (i, assignment)

def checkIfInX(i, assignment, dnf):
    for currI in range(i):
        (clause,_)=dnf[currI]
        shouldBreak=False
        for (v,b) in clause:
            if(assignment[v-1]!=b):
                shouldBreak=True
                break
        if (not(shouldBreak)):
            return False
        
    return True

def countValidAssignments(m, dnf,n,t,numberOfAssignments):
    count=0
    for _ in range(m):
        (i, assignment) = sampleRandom(dnf,n,t,numberOfAssignments)
        isValid = checkIfInX(i, assignment, dnf)
        if (isValid):
            count+=1
    return (count/m)*numberOfAssignments


def printDnf(dnf,n,t,numberOfAssignments):
    print("DNF\t","literals[n]=",n,"\tCaluses[t]=",t,"\tSize of Ω=",numberOfAssignments)
    for (clause,_) in dnf:
        print("\t",clause)

(dnf,n,t,numberOfAssignments)=getRandomDNF()

printDnf(dnf,n,t,numberOfAssignments)
print(countValidAssignments(10000, dnf,n,t,numberOfAssignments))

