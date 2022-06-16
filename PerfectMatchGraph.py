from sys import stdin
import random
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

def determinant(t):
    return np.linalg.det(np.array(t) )

def getRandom(min, max, lst):
    v = random.randint(min, max)
    lst.append(v)
    return v

def perfectMatch(matrix):
    res=[]
    t=tutteMatrix(matrix, lambda i,j : getRandom(-100,100,res))
    return (determinant(t) , matrix,t, res)


print("2 tests")
print(perfectMatch([[0,1,1],[1,0,1],[1,1,0]]))
print(perfectMatch([[0,0,0],[1,0,1],[1,1,0]]))
#grid
print("grid")
print(perfectMatch([[0,1,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,0,0,0],[1,0,0,0,1,0,1,0,0],[0,1,0,1,0,1,0,1,0],[0,0,1,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,1,0,1],[0,0,0,0,0,1,0,1,0]]))
#cycle
print("cycles")
print(perfectMatch([[0,1,0,0,1],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[1,0,0,1,0]]))
print(perfectMatch([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]))

print("break 4-cycle")
#random on 4-cycle
(det1, _, _, _)=perfectMatch([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
while(True):
    (det2, _, t, _)=perfectMatch([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    if(det2==0.0):
        print(det2, t)
        break