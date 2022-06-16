from sys import stdin
import random
import numpy as np
from heapq import heappop, heappush
import matplotlib.pyplot as plt
import math
import copy
from DP_TSP import DP_TSP
from MetricTSP import two_approximation, threeHalf_approximation

def haversine(v):
    return math.sin(v/2)^2

def distance(p1, p2):
    lon1, lat1 = p1
    lon2, lat2 = p2
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def parse_start():
    names=[]
    points=[]
    for (line_number, line) in enumerate(stdin):
        split = line.replace(" \n", "").split(" ")
        names.append(split[0])
        points.append((float(split[1]),  float(split[3])))
    return names, points

def randomPoints(n, maxX, maxY):
    points = [(random.randint(0,maxX), random.randint(0,maxY)) for i in range(n)]
    return [str(i) for i in points], points


def randomMetricGraph(points):
    n=len(points)
    graph=[[0 for v in range(n)] for v in range(n)]
    for i in range(n):
        for j in range(i,n):
            x1,y1 = points[i]
            x2,y2 = points[j]
            dist = math.pow(x1-x2, 2) + math.pow(y1-y2, 2)
            #dist= distance(points[i], points[j])
            graph[i][j]=dist
            graph[j][i]=graph[i][j]
    for i in range(n):
        graph[i][i]=0
    return (points, graph)

def split(points):
    x,y=[],[]
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x,y)

def plotAndPrint(names, points, ax, res, name):
    v,path=res
    print(name, v)
    print('\t', [names[i] for i in path])
    px,py = split(points)
    ax.plot(px,py,'bo')

    px2,py2 = split([points[i] for i in path])
    ax.plot(px2,py2,'r-')
    ax.set_title(name+", cost="+str(v) )
    print("")

def printTree(points, ax, treeEdges):
    for (v,i1,i2) in treeEdges:
        p1,p2=points[i1], points[i2]
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], 'k-', linewidth=3.0)


def main():
    names, points= parse_start()
    #names, points= randomPoints(8, 1000, 1000)

    points, g=randomMetricGraph(points)
    fig, axs = plt.subplots(3)
    fig.suptitle('TSP')

    plotAndPrint(names,points, axs[0], DP_TSP(g), "DP_TSP(g)")
    
    v,path, treeEdges, tour = two_approximation(g)
    printTree(points, axs[1], treeEdges)
    plotAndPrint(names,points, axs[1], (v,path), "two_approximation(g)")

    v,path, treeEdges, tour = threeHalf_approximation(g)
    printTree(points, axs[2], treeEdges)
    plotAndPrint(names,points, axs[2], (v,path), "threeHalf_approximation(g)")
    
    print("")
    print("")
    plt.show()

main()
