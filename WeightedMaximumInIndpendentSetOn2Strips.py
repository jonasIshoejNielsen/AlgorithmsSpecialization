from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
import math

    
class Column(object):
    def __init__(self, v1,v2, connected,edgesV1,edgesV2, prevColumn):
        self.v1 = v1
        self.v2 = v2
        self.connected=connected
        self.edgesV1=edgesV1
        self.edgesV2=edgesV2
        self.prevColumn=prevColumn
    def getVal(self,i):
        if(i==0):
            return self.v1
        return self.v2
    def printSelf(self):
        if(self.connected):
            print("Column", self.v1,"--", self.v2)
        else:
            print("Column", self.v1, self.v2)
        if(self.prevColumn is None):
            return
        for i in self.edgesV1:
                print('\t', self.v1,"--",self.prevColumn.getVal(i))
        for i in self.edgesV2:
            print('\t', self.v2,"--",self.prevColumn.getVal(i))

        self.prevColumn.printSelf()

def maxCompatible(edges,prevTake):
    res=[prevTake[0],prevTake[1],prevTake[2]]    #v1,v2, {v1,v2}
    for i in edges:
        res[i]=-math.inf
        res[2]=-math.inf

    return max(res)

def aux(c):
    if(c.prevColumn is None):
        sumBoth=-math.inf if (c.connected) else c.v1+c.v2    
        print(c.v1,c.v2,'\t',0,[c.v1,c.v2, sumBoth])
        return 0,[c.v1,c.v2, sumBoth]

    prevOut,prevTake=aux(c.prevColumn)

    sumOut=max([prevOut,max(prevTake)])

    sumV1=c.v1+max([prevOut,maxCompatible(c.edgesV1, prevTake)])
    sumV2=c.v2+max([prevOut,maxCompatible(c.edgesV2, prevTake)])
    
    sumBoth=c.v1+c.v2+max([prevOut,maxCompatible(c.edgesV1+c.edgesV2, prevTake)])
    if(c.connected):
        sumBoth=-math.inf
    #print(c.v1,c.v2,'\t',sumOut,[sumV1,sumV2, sumBoth])
    return sumOut,[sumV1,sumV2, sumBoth]


c1=Column(6,1,True,[],[],None)
c2=Column(12,7,False,[1],[0],c1)
c3=Column(90,12,True,[0,1],[],c2)
c4=Column(90,12,False,[1],[0],c3)

c4.printSelf()
print("")
resV,resLst=aux(c4)
print("res=",max(resV,max(resLst)))