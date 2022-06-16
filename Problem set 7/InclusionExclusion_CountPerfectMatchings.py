from sys import stdin
import random
import numpy as np
import math
import cmath
import copy
from scipy.optimize import linprog
from itertools import chain, combinations
import scipy.special

def randomGraph(n):
    res=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            res[i][j]=random.randint(0, 1)
            res[j][i]=res[i][j]
    for i in range(n):
        res[i][i]=0
    return res

def index(n,i,j):
    return i*n + j

def gridGraph(n, m):
    res=[[0 for v in range(n*m)] for v in range(n*m)]
    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(n):
                for j2 in range(m):
                    if(abs(i1-i2)+abs(j1-j2)>1 or abs(i1-i2)+abs(j1-j2)==0):
                        continue
                    res[index(m,i1,j1)][index(m,i2,j2)]=1
    #for i in range(n):
    #    res[i][i]=0
    return res



def countEdges(g, excluded):
    n=len(g)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if(g[i][j]==0):
                continue
            if(i in excluded or j in excluded):
                continue
            res+=1
    return res

def valueOfSubset(g, s):
    excluded={}
    for v in s:
        excluded[v]=True
    ms=countEdges(g, excluded)
    return math.pow(-1,len(s))*scipy.special.binom(ms, len(g)/2.0) 


def powerset(lst):
    #method for subsets: by https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset    #too lazy to do my own
    sets = chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))
    return sets


#inclusion exclusion
def countPerfectMatchings(g):
    if(len(g)%2!=0):
        print("error")
    sets=powerset([v for v in range(len(g))])
    count=0
    for s in sets:
        count+=valueOfSubset(g,s)
    return round(count) #to make smarter

def correctForSquare1(n,m):
    res = 1 
    for j in range(1,n+1):
        resInner=1
        for k in range(1,m+1):
            v1=4*math.pow(math.cos(math.pi*j/(n+1)), 2)
            v2=4*math.pow(math.cos(math.pi*k/(m+1)), 2)
            resInner*=math.pow(v1+v2, 0.25)
        res*=resInner
    return round(res)

def testCorrectGridMatrix(maxN,maxM):
    for n in range(1,maxN):
        for m in range(1,maxM):
            if(n*m%2!=0):
                continue
            g=gridGraph(n,m)
            alg=countPerfectMatchings(g)
            realRes1=correctForSquare1(n,m)
            if(alg != realRes1):
                print("error: n=",n, " m=",m)
                print("real=", realRes1)
                print("ALG=",alg)
                print("")
                return
#testCorrectGridMatrix(5,5)

#exercise 2, test the limit
n,m=9,2

print(countPerfectMatchings(gridGraph(n,m)), correctForSquare1(n,m))


"""
g=randomGraph(10)
for v in g:
    print(v)
print(countPerfectMatchings(g))
"""