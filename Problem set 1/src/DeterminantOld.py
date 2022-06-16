from sys import stdin
import random
import math
import numpy as np


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

def newtonCompute(r, l, traces, factorials):
    res = math.pow(traces[r-1],l) / (factorials[l]*math.pow(-r,l))
    return res

def determinant(m):
    #preperation
    n=len(m)
    traces=getTraces(m,n)
    factorials=getFactorials(n)
    
    #bad dynamic programming
    opt = [[0]*n for i in [0]*n]
    for r in range(1,n+1):
        previous = {}
        for w in range(1,n+1):
            res = 0
            for l in range(1,n+1):
                dif = w-(r*l)
                if (dif<0): break
                if (dif>=r): continue
                #todo: only add if [l*r] is not in it
                previous[l*r]= newtonCompute(r,l, traces, factorials)
                
                for rl in previous:
                    v = previous[rl]
                    dif = w-rl
                    if(dif==0):
                        res +=v
                    for d in range(1,dif+1):
                        if(d>=r):
                            break
                        v_d=opt[d-1][dif-1]
                        res+=v_d*v

            opt[r-1][w-1] = res
    #end
    determinant = 0
    for i in range(n):
        determinant+=opt[i][n-1]
    determinant*=math.pow(-1,n)
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
    n = random.randint(1, 7)
    determinant([[random.randint(1, 10) for v in range(n)] for v in range(n)])

testTestMatrices()

print("")
print("")
print("random")
for i in range(10):
    print("")
    testRandomMatrice()
