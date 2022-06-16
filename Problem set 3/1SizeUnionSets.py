import math
from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def getRandomListList():
    m=random.randint(2,500)
    n=random.randint(m,1000)
    lists=[]
    all=set([])
    numberElements=0
    for i in range(m):
        current=set([])
        m2=random.randint(1,m)
        for v in range(m2):
            v=random.randint(1,n)
            current.add(v)
            all.add(v)
        m2 = len(current)
        numberElements+=m2
        lists.append((list(current), m2))
    return (lists,n,m,numberElements, len(all))

def sampleRandom(lists,n,m,numberElements):
    i=0
    target=random.randint(0,numberElements)
    current=0
    for (lst,m2) in lists:
        current+=m2
        if(current>=target):
            break
        i+=1
    (lst,m2)=lists[i]
    assignment=lst[random.randint(0,m2-1)]
    return (i, assignment)

def checkIfInX(i, assignment, lists):
    for currI in range(i):
        (lst,_)=lists[currI]
        if (assignment in lst):
            return False
        
    return True

def countValidAssignments(r, lists,n,m,numberElements):
    count=0
    for _ in range(r):
        (i, assignment) = sampleRandom(lists,n,m,numberElements)
        isValid = checkIfInX(i, assignment, lists)
        if (isValid):
            count+=1
    return (count/r)*numberElements


beta=1/5
epsilon=1/5
for t in range(10):
    (lists,n,m,numberElements, result)=getRandomListList()
    r=math.ceil(3*m*math.log(2/beta)/(epsilon*epsilon))
    estimated=countValidAssignments(r, lists,n,m,numberElements)
    pct=100*countValidAssignments(r, lists,n,m,numberElements)/result
    if pct>100:
        print(pct%100, "%", "away from ",result)
    else:
        print(100-pct, "%", "away from ",result)


