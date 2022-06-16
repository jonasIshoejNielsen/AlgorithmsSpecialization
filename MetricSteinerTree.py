from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import math


def randomGraph(n, max_weight, edgeProp):
    randRange=1000
    edgeRange=float(randRange)*edgeProp
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            if(random.uniform(0,randRange)<=edgeRange):
                graph[i][j]=random.randint(1,max_weight)
                graph[j][i]=graph[i][j]
    for i in range(n):
        graph[i][i]=0
    return graph

def randomTerminals(n):
    return [random.randint(1,1000)>=300 for i in range(n)]


def toMetricSteinerTree(g):
    n=len(g)
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            graph[i][j]=path(g,i,j)[0]
            graph[j][i]=graph[i][j]
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

def minimumSpanningTree(g, terminals):
    n=len(g)
    explored = [0 for i in range(n)]
    edges = []
    treeEdges=[]
    tree=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        if(not(terminals[i])):
            continue
        for j in range(i,n):
            if(not(terminals[j])):
                continue
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

def MST_To_SteinerTree(g_tilde, g, treeEdges):
    edges={}
    graph=[[math.inf for v in range(n)] for v in range(n)]
    for (c,u,v) in treeEdges:
        p=path_vertices(path(g_tilde, u,v)[1], u, v)
        for(i,j) in p:
            e=(min(i,j),max(i,j))
            if(e in edges):
                continue
            graph[i][j]=g[i][j]
            graph[j][i]=graph[i][j]
            edges[e]=True
    terminals=[True for i in range(len(g))]
    return minimumSpanningTree(graph, terminals)[1]


n=4
g=randomGraph(n, 100, 1.0)
printGraph(g)
print("")
print("")
g_tilde=toMetricSteinerTree(g)
printGraph(g_tilde)
print("")
print("")
terminals=randomTerminals(n)
print("terminals=",terminals)
(tree, treeEdges) = minimumSpanningTree(g_tilde, terminals)
#printGraph(tree)
print("treeEdges=",treeEdges)

print("")
print("")
steinerTree=MST_To_SteinerTree(g_tilde, g, treeEdges)
print("steinerTree=",steinerTree)
cost_T=sum([c for (c,_,_) in steinerTree])
print("Cost T=",cost_T)
if(cost_T != math.inf):
    print(math.ceil(cost_T/2.0),"<=OPT<=",cost_T)
