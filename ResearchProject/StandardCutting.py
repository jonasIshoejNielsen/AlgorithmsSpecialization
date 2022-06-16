from sys import stdin
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull

def getPoints(n, xbound, ybound):
    return [[random.uniform(-xbound,xbound), random.randint(-ybound,ybound)] for i in range(n)]
def sort(points):
    points.sort()
    return points
def split(points):
    x,y=[],[]
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x,y)

def addPointToClosests(x,y,lines):
    bestLst,bestDist=None, None
    i=0
    for lst in lines:
        dist=math.pow(lst[0][1]-y,2)
        if(bestLst is None or bestDist>dist):
            bestLst=lst
            bestDist=dist
    bestLst.append((x,y))

def makeLines(px,py,numberLines):
    x_min,x_max=min(px),max(px)
    y_min,y_max=min(py), max(py)
    diff_y=(y_max-y_min)/numberLines
    
    linesStart  =[[(x_min,y_min+diff_y*i), (x_max,y_min+diff_y*i)] for i in range(numberLines)]
    lines       =[[(x_min,y_min+diff_y*i)] for i in range(numberLines)]
    for i in range(len(px)):
        x,y=px[i], py[i]
        addPointToClosests(x,y,lines)
    for line in lines:
        while(line[0][0]==line[1][0]):
            line.pop(0)
        if(line[-1][1]!=x_max):
            line.append((x_max,line[-1][1]))
    return linesStart,lines

def findPointOnLine(line,x):
    for i in range(1,len(line)):
        xy=line[i]
        if(xy[0]<x):
            continue
        if(xy[0]==x):
            return xy[1]
        xyprev=line[i-1]
        a=(xyprev[1]-xy[1])/(xyprev[0]-xy[0])
        b=xy[1]-a*xy[0]
        return a*x+b


def cut(px,py, numberLines):
    x_min,x_max=min(px),max(px)
    y_min,y_max=min(py), max(py)
    diff_y=(y_max-y_min)/numberLines
    linesStart,lines=makeLines(px,py,numberLines)
    linesToConnect=[[(x_min,y_min), (x_max,y_min)]]
    for line in lines:
        linesToConnect.append(line)
    linesToConnect.append([(x_min,y_max), (x_max,y_max)])
    verticalLines=[]
    for i in range(1,len(linesToConnect)-1):
        for (x,y) in linesToConnect[i]:
            y_high,y_low=findPointOnLine(linesToConnect[i-1],x),findPointOnLine(linesToConnect[i+1],x)
            k=(x,(y_low,y,y_high))
            verticalLines.append(k)

    return linesStart,lines,verticalLines


def main():
    points=sort(getPoints(100,200,200))
    px,py = split(points)
    linesStart,lines,verticalLines=cut(px,py, 10)
    for line in linesStart:
        (lx,ly)=split(line)
        plt.plot(lx,ly,"r-")
    for line in lines:
        (lx,ly)=split(line)
        plt.plot(lx,ly,"g-")
    for (x,ys) in verticalLines:
        plt.plot([x,x],[ys[0],ys[1]],"c:")
        plt.plot([x,x],[ys[1],ys[2]],"m--")
        
    plt.plot(px,py,'b.')
    
    plt.show()


main()