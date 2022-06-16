import math
from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def getUnitSquare():
    return [[(x-1,y-1) for y in range(3) for x in range(3)]]


unitSquare=getUnitSquare()


def samplePoint(inCircle, inSquare):
    radius = 1
    x=random.uniform(-radius,radius)
    y=random.uniform(-radius,radius)
    if (math.sqrt((x*x) + (y*y))<=radius):
        return (inCircle+1, inSquare+1)
    return (inCircle, inSquare+1)

def keepSampling(amount):
    inCircle, inSquare = 0, 0
    for i in range(amount):
        (inCircle, inSquare) = samplePoint(inCircle, inSquare)
    return (inCircle, inSquare)

n=[]
res1=[]
res2=[]
for i in range(10,10_000,10):
    (inCircle, inSquare) = keepSampling(i)
    n.append(i)
    res1.append(abs(math.pi - 4*inCircle/inSquare))
    res2.append(4*inCircle/inSquare)
plt.plot(n,res1, n,res2)
plt.show()
