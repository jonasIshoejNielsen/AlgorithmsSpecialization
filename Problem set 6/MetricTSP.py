from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import math
import copy


def randomMetricGraph(n, A):
    B=2*A-1     #IF range [A,B] for 2A > B then triangleEquality holds
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            graph[i][j]=random.randint(A,B)
            graph[j][i]=graph[i][j]
    for i in range(n):
        graph[i][i]=0
    return graph


def path_vertices(explored, u, v):
    (cost, fromN,toN) = explored[v]
    if (fromN == u):
        return [(u,v)]
    res=path_vertices(explored, u, fromN)
    res.append((fromN, toN))
    return res

def path(g, u,v):
    explored = {}
    frontier = []
    if(u==v):
        return (0,explored)
    for i in range(len(g[u])):
        if(g[u][i]>=0):
            heappush(frontier, (g[u][i], u,i))
    while(frontier != []):
        (cost, fromN,toN) = heappop(frontier)
        if toN in explored:
            continue
        explored[toN] = (cost, fromN,toN)
        if v in explored:
            return (explored[v][0], explored)
        for i in range(len(g[toN])):
            if(g[toN][i]>=0):
                heappush(frontier, (g[toN][i]+cost, toN,i))
    print("inf=",u,v,explored)
    return (math.inf, explored)


def printGraph(g):
    for i in g:
        print(i)
def printCost(g,u,v):
    (cost, explored)=path(g,u,v)
    print("Cost:",u,v,"=",cost)
    if(cost is not math.inf):
        print('\t', path_vertices(explored, u, v))

def minimumSpanningTree(g):
    n=len(g)
    explored = [0 for i in range(n)]
    edges = []
    treeEdges=[]
    tree=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            heappush(edges, (g[i][j], i,j))
    group=1
    while(edges != []):     #todo stop when explored n-1
        (cost, n1, n2) = heappop(edges)
        if(cost == math.inf):
            continue
        if(n1 == n2):
            continue
        if (explored[n1]>0 and explored[n1]==explored[n2]):
            continue
        if(explored[n1]>0 and explored[n2]==0):
            explored[n2] = explored[n1]
        elif(explored[n2]>0 and explored[n1]==0):
            explored[n1] = explored[n2]
        elif(explored[n2]==0 and explored[n1]==0):
            explored[n1]=group
            explored[n2]=group
            group+=1
        else:
            oldGroup=explored[n1]
            for i in range(len(explored)):
                if (explored[i]==oldGroup):
                    explored[i]=explored[n2]
        treeEdges.append((cost, n1, n2))
        tree[n1][n2]=cost
        tree[n2][n1]=cost
    return (tree, treeEdges)

def doubeTree(tree):
    n=len(tree)
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(0,n):
            graph[i][j]=2 if (tree[i][j]>0) else 0
    return graph


def getNext(curr, missing):
    for i in range(len(missing)):
        if (missing[curr][i]>0):
            return i
    return None

def combineTour(attachment, tour):
    (wrapperTour, i)=attachment
    return wrapperTour[0:i]+tour+wrapperTour[i:len(wrapperTour)]

def eulerianTour(dtree):
    n=len(dtree)
    missing=[[dtree[v][u] for u in range(n)] for v in range(n)]
    needed=int(sum([sum(lst) for lst in dtree ])/2)
    tour=[]
    curr=0
    attachment=None
    while(needed>0):
        if(curr >=len(missing)):
            curr=0
        next=getNext(curr,missing)
        if(next is None):
            if(len(tour)==0):
                curr+=1
                continue
            if (attachment is not None):
                tour = combineTour(attachment, tour)
            for i in range(len(tour)):
                if (getNext(tour[i][0], missing) is not None):
                    curr=tour[i][0]
                    attachment = (tour, i)
                    tour=[]
                    break
            continue
        missing[curr][next] -=1
        missing[next][curr] -=1
        tour.append((curr,next))
        curr=next
        needed-=1
    if (attachment is not None):
        tour = combineTour(attachment, tour)
    return tour

def shourCutTour(tour, n):
    explored = [False for i in range(n)]
    path=[]
    explored[tour[0][0]]=True
    prev=None
    for (fromN,toN) in tour:
        if (explored[toN]):
            prev=path[len(path)-1][1]
            continue
        if (prev is None):
            path.append((fromN,toN))
        else:
            path.append((prev,toN))
            prev=None
        explored[toN]=True
    path.append((path[len(path)-1][1], path[0][0]))
    return path

def sizeOfTour(tour, g):
    sum=0
    for (i,j) in tour:
        sum+=g[i][j]
    return sum

def getOddDegreeVertexes(tree,g):
    oddDegrees=[]
    n=len(g)
    for i in range(n):
        sum=0
        for j in range(n):
            if(tree[i][j]>0):
                sum+=1
        if (sum%2==1):
            oddDegrees.append(i)
    return oddDegrees

def getMinimumFrom(oddDegrees, g):
    if(len(oddDegrees)==0):
        return (0,[])
    bestVal, bestM=math.inf, []
    for i in oddDegrees:
        for j in oddDegrees:
            if (i==j):
                continue
            copyOddDegrees = copy.copy(oddDegrees)
            copyOddDegrees.remove(i)
            copyOddDegrees.remove(j)
            (val,m) = getMinimumFrom(copyOddDegrees,g)
            val+=g[i][j]
            m.append((i,j))
            if(val<bestVal):
                bestVal=val
                bestM=m
    return (bestVal, bestM)

def minimumWeightPerfectMatchingOffOdd(tree,g,treeEdges):
    oddDegrees=getOddDegreeVertexes(tree,g)
    (val,m)=getMinimumFrom(oddDegrees, g)
    #combining
    n=len(g)
    mut=[[1 if (tree[u][v]>0) else 0 for u in range(n)] for v in range(n)]
    for (u,v) in m:
        mut[u][v]+=1
        mut[v][u]=mut[u][v]

    return (val,mut)

def toDFPath(path):
    return [path[0][0]]+[v for (u,v) in path]

def two_approximation(g):
    (tree, treeEdges) = minimumSpanningTree(g)
    #print("treeEdges=",treeEdges)
    #printGraph(tree)
    dtree=doubeTree(tree)
    #printGraph(dtree)

    tour=eulerianTour(dtree)
    #print("eulerianTour=",tour)

    shourCut=shourCutTour(tour, len(g))
    return (sizeOfTour(shourCut, g), toDFPath(shourCut), treeEdges, tour)


def threeHalf_approximation(g):
    (tree, treeEdges) = minimumSpanningTree(g)
    #print("treeEdges=",treeEdges)
    #printGraph(tree)

    (v,mut)=minimumWeightPerfectMatchingOffOdd(tree,g,treeEdges)
    #printGraph(mut)

    tour=eulerianTour(mut)
    #print("eulerianTour=",tour)
    shourCut=shourCutTour(tour, len(g))
    return (sizeOfTour(shourCut, g), toDFPath(shourCut), treeEdges, tour)


def main():
    for i in range(4):
        n=4
        g=randomMetricGraph(n, 100)
        printGraph(g)
        print("results:")
        print(two_approximation(g))
        print(threeHalf_approximation(g))
        print("")
        print("")
#main()
