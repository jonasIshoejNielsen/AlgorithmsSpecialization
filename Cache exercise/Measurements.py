from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import math
import time
import matplotlib.pyplot as plt
import statistics


def randomMatrix(n):
    lst=[v for v in range(n)]
    res=[]
    while len(lst)>0:
        res.append(lst.pop(random.randint(0, len(lst)-1)))
    return np.array(res)

def runTest(lst):
    i=0
    for t in range(len(lst)):
        i=lst[i]
    return i


def oneTestTime(n):
    lst=randomMatrix(n)
    start_time = time.time()
    v=runTest(lst)
    end_time=time.time()
    return v,(end_time - start_time)


def test(rounds, increases, tests):
    x,results=[], []
    v=0
    for round in range(2,rounds+1):
        n=round*increases
        curr=[]
        for i in range(tests):
            res1,time=oneTestTime(n)
            v+=res1
            curr.append(time)
        x.append(n)
        results.append(statistics.median(curr))
        print(n)
    return x, results



#print(oneTestTime(1_000_000))

#print(oneTestTime(10_000_000))

px,py=test(100, 50,50)

plt.plot(px,py,'bo')
#plt.xscale('log',base=2) 
plt.show()
