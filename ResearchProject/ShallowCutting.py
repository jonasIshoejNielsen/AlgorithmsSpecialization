from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull
from ConvexHull import convexHull

def getPoints(n, xbound, ybound):
    return [[random.uniform(-xbound,xbound), random.uniform(-ybound,ybound)] for i in range(n)]
def sort(points):
    points.sort()
    return points
def split(points):
    x,y=[],[]
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x,y)
def plotFunctions(fs,linespace):
    i=0
    for ab in fs:
        i+=1
        y=ab[0]*linespace+ab[1]
        plt.plot(linespace, y, "k-")

def getSuitable(points, fs, B,C, k):
    n=len(fs)
    maxLevel=B*k
    res=[]
    for p in points:
        level=0
        for ab in fs:
            if(ab[0]*p[0]+ab[1]<=p[1]):
                level+=1
        if(level<=maxLevel):
            res.append(p)
    return res

def tryBCK(points, fs, B,C,k):
    suitablePoints=getSuitable(points, fs, B,C,k)
    Cmark1=len(suitablePoints)*B*k/len(fs)
    goalPoints=getSuitable(points, fs, 1,C,k)
    Cmark2=len(goalPoints)*B*k/len(fs)
    Cmark=max(Cmark1,Cmark2)
    size1=Cmark*len(fs)/(B*k)
    size2=Cmark*len(fs)/(k)
    xuh,yuh=split(convexHull(suitablePoints, True))

    #Plot:
    maxLevel=B*k
    plt.title('B='+str(B)+'   C='+str(C)+'   k='+str(k)+'   maxLevel='+str(maxLevel)+'   Cmark='+str((Cmark, Cmark1,Cmark2))+'   SizeVin='+str((len(suitablePoints),size1))+'   SizeVout='+str((len(goalPoints),size2)))
    px,py=split(points)
    linespace=np.linspace(min(px),max(px),100)
    plotFunctions(fs,linespace)
    spx,spy=split(suitablePoints)
    gpx,gpy=split(goalPoints)
    plt.plot(px,py,'b.')
    plt.plot(spx,spy,'r.')
    plt.plot(gpx,gpy,'g.')
    plt.plot(xuh,yuh, "g-", linewidth=4)
    for xc in xuh:
        plt.axvline(x=xc)
    plt.show()



points=getPoints(10000,100,700)
points=sort(points)
px,py=split(sort(points))
fs=getPoints(100,5,700)

for i in range(4):
    B,C,k=random.randint(6,10),random.randint(1,10),random.randint(1,10)
    tryBCK(points, fs, B,C,k)


