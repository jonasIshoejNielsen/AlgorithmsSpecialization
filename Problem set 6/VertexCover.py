from sys import stdin
import random
import numpy as np
import copy
from scipy.optimize import linprog


def randomGraph(n):
    res=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            prop=1.0/2.0
            randRange=1000
            if(random.uniform(0,randRange)<=randRange*prop):
                res[i][j]=1
                res[j][i]=1
    for i in range(n):
        res[i][i]=0
    return res


def randomStar(n):
    res=[[0 for v in range(n)] for v in range(n)]
    v = random.randint(0, n-1)
    for i in range(n):
        res[i][v]=1
        res[v][1]=1
    res[v][v]=0
    return res


def randomDisjointedEdges(n):
    res=[[0 for v in range(n)] for v in range(n)]
    
    vertices=[i for i in range(len(g))]
    while(len(vertices)>1):
        i=vertices.pop(random.randint(0,len(vertices)-1))
        j=vertices.pop(random.randint(0,len(vertices)-1))
        res[i][j]=1
        res[j][i]=1
    return res

def perfectlyDense(n):
    res=[[1 for v in range(n)] for v in range(n)]
    for i in range(n):
        res[i][i]=1
    return res

def vertexCoverApprox(gPrime):
    g=copy.deepcopy(gPrime)
    M=[]
    resultingVertices=[]
    vertices=[i for i in range(len(g))]
    while(len(vertices)>0):
        v=vertices.pop(random.randint(0,len(vertices)-1))
        for i in range(len(g)):
            if(g[v][i]==1):
                M.append((v+1,i+1))
                resultingVertices.append(v+1)
                resultingVertices.append(i+1)
                for j in range(len(g)):
                    g[v][j]=0
                    g[i][j]=0
                    g[j][v]=0
                    g[j][i]=0
                vertices = list(filter(lambda j: j!=i, vertices))
    #return len(M)*2, M,
    return len(resultingVertices), resultingVertices

def arrayIfNotNone(ar):
    if(ar is None or len(ar)==0):
        return None
    return np.array(ar)

def runLP(c, isMinimize, A_ub=None, b_ub=None, A_eq=None, b_eq=None):
    return linprog(np.array(c) if isMinimize else -np.array(c), A_ub=arrayIfNotNone(A_ub), b_ub=arrayIfNotNone(b_ub), A_eq=arrayIfNotNone(A_eq), b_eq=arrayIfNotNone(b_eq))

def lpTest():
    #https://www.youtube.com/watch?v=uuosEqyLJiM&ab_channel=IPSA-IntroductiontoProgramming
    c=[3,2]
    A_ub=[[2,1], [-5,-6]]
    b_ub=[10,-4]
    A_eq=[[-3,7]]
    b_eq=[8]
    res=runLP(c, False, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)
    print(res)
    print(res["x"])



def LP_vertex_cover(g):
    isMinimize=True
    n=len(g)
    c=[1 for i in range(n)]     #since no weights, otherwise w(i) instead of 1
    A_ub=[]
    b_ub=[]
    for i in range(n):
        for j in range(i+1,n):
            if(g[i][j]>0):
                A_curr=[0 for i in range(n)]
                A_curr[i]=-1
                A_curr[j]=-1
                A_ub.append(A_curr)
                b_ub.append(-1)

    xs=runLP(c, isMinimize, A_ub=A_ub, b_ub=b_ub)["x"]
    vertices=[]
    for i in range(n):
        if(xs[i]>=0.5):
            vertices.append(i)
    return len(vertices), vertices, xs


#lpTest()
g=randomGraph(5)
g=randomStar(5)
g=randomDisjointedEdges(5)
for i in range(2):
    g=randomGraph(3)
    #g=[[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    #g=[[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    count1, vertices1=vertexCoverApprox(g)
    count2, vertices2, xs=LP_vertex_cover(g)
    print(g)
    print(count1, vertices1)
    print(count2, vertices2, xs)
    print("")