from sys import stdin
import random
import math
import numpy as np
from FFT import fft, ifft, multiply2Polynomials, roundLst


def tutteMatrix(g, randomVariable):
    n=len(g)
    res=[[0]*n for v in [0]*n]
    for i in range(n):
        for j in range(n):
            if (g[i][j] == 0):
                res[i][j]=0
            elif (i<j):
                res[i][j]=randomVariable(i,j)
            else:
                res[i][j]=-res[j][i]
    return res

def NP_determinant(t):
    return np.linalg.det(np.array(t) )

def getTrace(m,n):
    res = 0
    for i in range(n):
        res += m[i][i]
    return res

def getTraces(m,n):
    currMatrix=1
    res = []
    for i in range(n):
        currMatrix = np.dot(np.array(m), currMatrix)
        res.append(getTrace(currMatrix,n))
    return res

def getFactorials(n):
    res = [0]
    curr = 1
    for i in range(1,n+1):
        curr*=i
        res.append(curr)
    return res

def newtonCompute(l, e, traces, factorials):
    res = math.pow(traces[l-1],e) / (factorials[e]*math.pow(-l,e))
    return res

def determinant(m):
    #preperation
    n=len(m)
    traces=getTraces(m,n)
    factorials=getFactorials(n)
    
    #polynomial creation
    polynomials=[]
    for l in range(1,n+1):
        polynomial=[1]
        for e in range(1,n+1):
            if(e%l==0):
                polynomial.append(newtonCompute(l,int(e/l), traces, factorials))
            else:
                polynomial.append(0)
        polynomials.append(polynomial)
        
    #Polynomial multiplication
    while(len(polynomials)!=1):
        p1=polynomials.pop(0)
        p2=polynomials.pop(0)
        product=multiply2Polynomials(p1, p2)
        polynomials.append(product[0:n+1])
    
    determinant=polynomials[0][n].real*math.pow(-1,n)
    print("computed determinant=", determinant)
    print("Real determinant(np)=", NP_determinant(m))
    return determinant




def testTestMatrices():
    determinant([[2,4],[4,5]])
    print("")
    determinant([[2,4,6],[4,5,1], [2,1,5]])
    print("")
    determinant([[2,4,6,5],[4,5,1,8], [2,1,5,1], [3,6,2,1]])
    print("")
    determinant([[2,4,6,5,3],[4,5,1,8,3], [2,1,5,1,3], [3,6,2,1,3], [3,6,2,1,5]])

def testRandomMatrice():
    n = random.randint(1, 5)
    determinant([[random.randint(1, 10) for v in range(n)] for v in range(n)])

testTestMatrices()

print("")
print("")
print("random")
for i in range(10):
    print("")
    testRandomMatrice()
