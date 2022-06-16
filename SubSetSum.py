from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull

def compute(sortedValues, T):
    M=[[False for v in range(T+1)] for i in range(len(sortedValues)+1)]
    for i in range(1,len(sortedValues)+1):
        curr=sortedValues[i-1]
        for v in range(T+1):
            print(curr,i,v)
            if(v==curr):
                M[i][v]=True
            elif(M[i-1][v]):
                M[i][v]=True
            elif(M[i-1][v-curr]):
                M[i][v]=True
            print("\t",M[i][v])
    return M

def traceBack(sortedValues, M):



M=compute([1,2,3], 5)
print(compute([1,2,3], 5))
            


