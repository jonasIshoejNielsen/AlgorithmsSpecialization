from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def hash(u, h):
    random.seed(u+h)
    return random.randint(0, 2) -1

def secondFrequency(n,m):
    h=random.randint(0,1000)
    res=0
    frequencies=[0 for i in range(m)]
    for i in range(n):
        xi=random.randint(0,m)
        frequencies[xi]+=1
        res+=hash(xi,h)
    real = sum([v*v for v in frequencies])
    return (res*res, real)

print(secondFrequency(10000, 10000))