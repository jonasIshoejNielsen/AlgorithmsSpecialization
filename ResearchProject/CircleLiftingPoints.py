from sys import stdin
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull

def getPoints(n, xbound, ybound):
    return [[random.randint(-xbound,xbound), random.randint(-ybound,ybound)] for i in range(n)]

def getCircle(xbound, ybound):
    return [random.randint(-10,10), random.randint(-ybound,ybound), random.randint(xbound/5, xbound/2)]

def split(points):
    res=[[] for i in range(len(points))]
    for p in points:
        for i in range(len(p)):
            res[i].append(p[i])
    return res

def pTpUnitParaboloid(points):
    return ([(p[0], p[1], (p[0]**2 + p[1]**2)) for p in points])

def circleToUnitParaboloid(c):
    return (2*c[0], 2*c[1], -(c[0]**2) -(c[1]**2) + c[2]**2)


def toHyperPlane(pt):
    return [(p[0], p[1], -p[2]) for p in pt]

def plotCircle(circle):
    x = np.arange(-200, 200, 0.01)
    v=(-(circle[0]**2) - 2*circle[0]*x + (circle[2]**2) - (x**2))**0.5
    #v=[math.sqrt(p) for p in v]
    plt.plot(x,circle[1]-v, color='r')
    plt.plot(x,circle[1]+v, color='r')


def plotHyperPlanes(pTT, ax, centerX=0, centerY=0, size=100):
    xx, yy = np.meshgrid(range(centerX-size,centerX+size), range(centerY-size,centerY+size))
    for p in pTT:
        ax.plot_surface(xx, yy, p[0]*xx + p[1]*yy+ p[2], alpha=0.3)



def main():
    pointRange=200
    n=5
    points=getPoints(n,pointRange,pointRange)
    pT = pTpUnitParaboloid(points)
    pTT = toHyperPlane(pT)

    circle=getCircle(pointRange,pointRange)
    cT=circleToUnitParaboloid(circle)
    cTT=toHyperPlane([cT])[0]
    print(circle)
    print(points)



    #Vin
    pSplit = split(points)
    plt.plot(pSplit[0],pSplit[1],'bo')
    plotCircle(circle)
    plt.show()

    #Vin*
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    pTSplit = split(pT)
    ax.scatter3D(pTSplit[0],pTSplit[1],pTSplit[2]);
    plotHyperPlanes([cT], ax, size=pointRange)
    print(cT)
    plt.show()

    
    #Vin**
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    print("cTT",cTT)
    plotHyperPlanes(pTT, ax, centerX=cTT[0], centerY=cTT[1],  size=50)
    ax.scatter3D(cTT[0],cTT[1],cTT[2]);
    plt.show()

main()