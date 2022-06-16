from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import copy

def randomLstToN(n):
    curr = [i+1 for i in range(n)]
    res = []
    while (len(curr)!=0):
        res.append(curr.pop(random.randint(0,len(curr)-1)))
    return res

def leftRightMinima(lst):
    currMinimum = len(lst)*2
    changes=0
    for i in lst:
        if (currMinimum<i):
            continue
        currMinimum=i
        changes+=1
    return changes


def hn(n):
    hn=sum([1/i for i in range(1,n+1)])
    return hn

ns=[]
lst=[]
hns=[]
for n in range(5,5000,5):
    curr = 0
    repeats=50
    for i in range(repeats):
        curr+=leftRightMinima(randomLstToN(n))
    print(n)
    ns.append(n)
    lst.append(curr/repeats)
    hns.append(hn(n))
plt.plot(ns,lst, 'r--',ns,hns, 'bs')
plt.show()