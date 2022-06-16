from sys import stdin
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from scipy.spatial import ConvexHull

def makeTrapezoid(xs, y1s, y2s):
    x_min,x_max=(min(xs),max(xs))
    return [(x_min, y1s[0]), (x_min, y1s[1]), (x_max, y2s[1]),(x_max, y2s[0]), (x_min, y1s[0])]

def getTrapezoid(xbound, ybound):
    xs=[]
    ys=[]
    for i in range(2):
        x1=random.uniform(0,int(xbound/2))
        xs.append(x1)
        y1=random.uniform(xbound/10.0,int(ybound/2))
        y2=y1+random.uniform(0,int(ybound/2))
        ys.append((y1,y2))
    return makeTrapezoid(xs, ys[0], ys[1])


def getLine(abound, bbound):
    return (random.uniform(-abound,abound), random.uniform(-bbound,bbound))

def intersectionBetween(point1, point2, fs):
    a=(point1[1]-point2[1])/(point1[0]-point2[0])
    b=point1[1]-a*point1[0]
    x=(b-fs[1]) / (fs[0]-a)
    return (x, a*x+b)

def yAtXBetween(point1, point2, x):
    a=(point1[1]-point2[1])/(point1[0]-point2[0])
    b=point1[1]-a*point1[0]
    return a*x+b

def intersection(trapezoid, fs):
    x1,x2=trapezoid[0][0], trapezoid[2][0]
    y1_min, y1_max=trapezoid[0][1], trapezoid[1][1]
    y2_min, y2_max=trapezoid[3][1], trapezoid[2][1]
    fs_x1=fs[0]*x1+fs[1]
    fs_x2=fs[0]*x2+fs[1]
    first_between   =fs_x1<y1_max and fs_x1>y1_min
    second_between  =fs_x2<y2_max and fs_x2>y2_min
    if((fs_x1>y1_max and fs_x2 > y2_max) or (fs_x1<y1_min and fs_x2 < y2_min)):
        print("type0", (fs_x1>y1_max and fs_x2 > y1_max), (fs_x1<y1_min and fs_x2 < y1_min), first_between, second_between)
        return ([], [trapezoid])
    if(first_between and second_between):
        print("type1")
        return ([(x1, fs_x1), (x2, fs_x2)], [makeTrapezoid([x1,x2], [fs_x1, y1_max], [fs_x2, y2_max]), makeTrapezoid([x1,x2], [y1_min, fs_x1], [y2_min,fs_x2])])
    if(first_between):
        print("type2", (fs_x2>y2_max))
        (ix,iy)= intersectionBetween((x1,y1_max), (x2,y2_max), fs) if (fs_x2>y2_max) else intersectionBetween((x1,y1_min), (x2,y2_min), fs)
        othery=yAtXBetween((x1,y1_min), (x2,y2_min), ix) if (fs_x2>y2_max) else yAtXBetween((x1,y1_max), (x2,y2_max), ix)
        ysTop,ysBottom = ([min(iy,othery), max(iy,othery)], [iy, iy]) if (fs_x2>y2_max) else ([iy, iy], [min(iy,othery), max(iy,othery)])
        return ([(x1, fs_x1), (ix,iy)], 
            [makeTrapezoid([x1,ix], [y1_min, fs_x1], ysTop), 
            makeTrapezoid([x1,ix], [fs_x1, y1_max], ysBottom), 
            makeTrapezoid([ix, x2], [min(iy,othery), max(iy,othery)], [y2_min, y2_max])])
    if(second_between):
        print("type3",(fs_x1>y1_max))
        (ix,iy)= intersectionBetween((x1,y1_max), (x2,y2_max), fs) if (fs_x1>y1_max) else intersectionBetween((x1,y1_min), (x2,y2_min), fs)
        othery=yAtXBetween((x1,y1_min), (x2,y2_min), ix) if (fs_x1>y1_max) else yAtXBetween((x1,y1_max), (x2,y2_max), ix)
        ysTop,ysBottom = ([min(iy,othery), max(iy,othery)], [iy, iy]) if (fs_x1>y1_max)  else ([iy, iy], [min(iy,othery), max(iy,othery)])
        return ([(ix,iy), (x2, fs_x2)], 
            [makeTrapezoid([x1,ix], [y1_min, y1_max], [min(iy,othery), max(iy,othery)]), 
            makeTrapezoid([ix, x2], ysTop, [y2_min, fs_x2]), 
            makeTrapezoid([ix, x2], ysBottom, [fs_x2, y2_max])])
    print("type4")
    firstIsTop=True
    (ix1,iy1) = intersectionBetween((x1,y1_max), (x2,y2_max), fs)
    (ix2,iy2) = intersectionBetween((x1,y1_min), (x2,y2_min), fs)
    if(ix1>ix2):
        firstIsTop=False
        (ix3,iy3) = (ix1,iy1)
        (ix1,iy1) = (ix2,iy2)
        (ix2,iy2) = (ix3,iy3)
    othery1=yAtXBetween((x1,y1_min), (x2,y2_min), ix1) if (firstIsTop) else yAtXBetween((x1,y1_max), (x2,y2_max), ix1)
    othery2=yAtXBetween((x1,y1_max), (x2,y2_max), ix2) if (firstIsTop) else yAtXBetween((x1,y1_min), (x2,y2_min), ix2)
    #todo
    return ([(ix1,iy1), (ix2,iy2)], 
        [makeTrapezoid([x1,ix1], [y1_min, y1_max], [min(iy1,othery1), max(iy1,othery1)]),
        makeTrapezoid([ix1,ix2], [min(iy1,othery1), max(iy1,othery1)], [iy2, iy2]),
        makeTrapezoid([ix1,ix2], [iy1, iy1], [min(iy2,othery2), max(iy2,othery2)]),
        makeTrapezoid([ix2,x2], [min(iy2,othery2), max(iy2,othery2)], [y2_min, y2_max])
        ])


#VISUALIZING
def split(points):
    x,y=[],[]
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x,y)
def plotFunctions(fs,linespace):
    y=fs[0]*linespace+fs[1]
    plt.plot(linespace, y, "k-")

def visualize(trapezoid, fs, intersect, newTrapezoids):
    plt.title(len(newTrapezoids))
    px,py=split(trapezoid)
    ix,iy=split(intersect)
    linespace=np.linspace(min(px)*0.9,max(px)*1.1,100)
    plotFunctions(fs,linespace)
    plt.plot(px,py,'b-')
    lineColors=['g-', 'b-', 'r-', 'm-']
    for i in range(len(newTrapezoids)):
        tx,ty=split(newTrapezoids[i])
        lineColor = lineColors[i]
        plt.plot(tx,ty,lineColor)
    plt.plot(ix,iy,'y-')
    plt.show()


while(True):
    trapezoid=getTrapezoid(100,700)
    trapezoid=[(23.77243941101199, 18.86070903450193), (23.77243941101199, 198.6502127825493), (35.57986129548944, 426.6043224856684), (35.57986129548944, 123.46711704716226), (23.77243941101199, 18.86070903450193)]
    fs=getLine(20,900)
    intersect, newTrapezoids=intersection(trapezoid, fs)
    if(len(newTrapezoids)==4):
        #print(trapezoid)
        print("intersect=",intersect)
        visualize(trapezoid, fs, intersect, newTrapezoids)
