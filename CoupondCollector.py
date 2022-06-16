from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def start(n):
    collected = [0 for i in range(n)]
    have = 0
    tried=0
    while(have <n):
        tried+=1
        new = random.randint(0,n-1)
        if(collected[new]==1):
            continue
        collected[new]=1
        have += 1
    return tried

def harmonicNumber(n):
    res = 0
    for k in range(1,n+1):
        res+=1/k
    return res

ns = []
res=[]
expected=[]

for n in range(0,2000,10):
    ns.append(n)
    curr = 0
    repeats=5
    for i in range(repeats):
        curr += start(n)
    res.append(curr/repeats)
    expected.append(n*harmonicNumber(n))
plt.plot(ns,res, ns, expected)
plt.xlabel("#Types of couponds")
plt.ylabel("Boxes bought")
plt.show()
