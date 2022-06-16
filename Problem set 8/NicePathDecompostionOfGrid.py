from sys import stdin
import random
import numpy as np
import math
import cmath
import copy
from scipy.optimize import linprog
from itertools import chain, combinations
import scipy.special

class Node:
    def __init__(self, bag, parent):
        self.bag=bag
        self.parent=parent
    def printIndexed(self,n):
        print([index(n,i,j) for i,j in self.bag])
        if(self.parent is not None):
            self.parent.printIndexed(n)
    def printValue(self):
        print(self.bag)
        if(self.parent is not None):
            self.parent.printValue()


def index(n,i,j):
    return i*n + j

def toPathDecomposition(nIn, mIn):
    n=min(mIn,nIn)
    m=max(mIn,nIn)
    bag=[]
    currNode=Node(bag,None)
    for i in range(m):
        for j in range(n):
            if(len(bag)==n+1):
                bag=bag[1:]
                currNode=Node(bag,currNode)
            bag=bag+[(i,j)]
            currNode=Node(bag,currNode)
    while(len(bag)!=0):
        bag=bag[1:]
        currNode=Node(bag,currNode)
    return n,m,currNode


def main():
    n,m=3,3
    n,m,node=toPathDecomposition(n,m)
    node.printValue()
    print("")
    node.printIndexed(n)

#main()