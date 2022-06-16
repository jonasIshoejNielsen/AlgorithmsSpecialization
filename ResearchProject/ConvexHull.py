from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull

def getPoints(n, xbound, ybound):
    return [[random.randint(-xbound,xbound), random.randint(-ybound,ybound)] for i in range(n)]
def getFunction(n, xbound, ybound):
    return [[random.randint(-xbound,xbound), random.randint(-ybound,ybound)] for i in range(n)]

def sort(points):
    points.sort()
    return points
def split(points):
    x,y=[],[]
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x,y)

def addToHull(hull, x,y, uh):
    if (len(hull) <2):
        hull.append((x,y))
        return False
    x2,y2=hull[len(hull)-2]
    x1,y1=hull[len(hull)-1]
    if (x1-x2==0):
        hull.pop(len(hull)-1)
        return True
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    if ((a*x+b<y and uh) or (a*x+b>y and not(uh))):
        hull.pop(len(hull)-1)
        return True
    hull.append((x,y))
    return False

def convexHull(sortedPoints, uh):
    hull=[]
    px,py = split(sortedPoints)
    for (x,y) in sortedPoints:
        if(len(hull)<=1):
            hull.append((x,y))
            continue
        nremoving=True
        while(nremoving):
            nremoving=addToHull(hull, x,y, uh)
            continue
    return hull

def correctHull(points):
    npPoints = np.array(points)
    hull = ConvexHull(npPoints)

    plt.plot(npPoints[:,0], npPoints[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(npPoints[simplex, 0], npPoints[simplex, 1], 'k-')
    plt.show()

def main():
    points=getPoints(50,200,200)
    points=sort(points)
    px,py = split(points)
    xuh,yuh = split(convexHull(points,True))
    xbh,ybh = split(convexHull(points,False))

    correctHull(points)
    plt.plot(px,py,'bo', xuh,yuh, xbh,ybh)
    for xc in xuh:
        plt.axvline(x=xc)


    plt.show()

main()