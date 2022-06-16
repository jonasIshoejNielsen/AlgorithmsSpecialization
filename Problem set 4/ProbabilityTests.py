from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def randomBool():
    return random.randint(0,999999) % 2 == 0

def test(n,a):
    success=0
    for i in range(n):
        if (randomBool()):
            success+=1
    return success>=a


numberofTests=10000
k=0
for i in range(numberofTests):
    if (test(100,55)):
        k+=1
print(float(k)/float(numberofTests))


k=0
for i in range(numberofTests):
    if (test(1000,550)):
        k+=1
print(float(k)/float(numberofTests))

