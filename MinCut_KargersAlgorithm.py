from sys import stdin
from functools import lru_cache
import random
import copy
import math



class Edge(object):
    def __init__(self, fromN, toN):
        self.fromN  = fromN
        self.toN    = toN
        self.name   = str(self.fromN.name) +" - "+str(self.toN.name)
        
    def __str__(self):
        return self.name
        
    
class Node(object):
    def __init__(self, name):
        self.edges = []
        self.name = name
    
    def addEdgeTo(self, node):
        edge = Edge(self, node)
        self.edges.append(edge)
        return edge
    
    def concatenate(self, other, newNode):
        for edge in self.edges:
            if(edge.toN == other):
                continue
            edge.toN.replaceDesintaionEdges(self,newNode)
            newNode.edges.append(edge)
            edge.fromN = newNode
    def replaceDesintaionEdges(self, old, newToN):
        for edge in self.edges:
            if(edge.toN != old):
                continue
            edge.toN = newToN
              
    def printSelf(self):
        print(self.name)
        for e in self.edges:
            print("    " + str(e))

class Case(object):
    def __init__(self, numberOfNodes):
        self.nodes      = [Node(i) for i in range(numberOfNodes)]     #ignore nodes[0]

    def addEdgeFromTo(self, start, end):
        endNode = self.nodes[end]
        edge = self.nodes[start].addEdgeTo(endNode)
    
    def concatenate(self):
        n=len(self.nodes)
        node1=self.nodes.pop(random.randint(0,n-1))
        node2=self.nodes.pop(random.randint(0,n-2))
        newNode=Node([node1.name, node2.name])
        node1.concatenate(node2, newNode)
        node2.concatenate(node1, newNode)
        self.nodes.append(newNode)

    def printCase(self):
        print("S:")
        for n in self.nodes:
            n.printSelf()

def createCase(n, lst):
    case = Case(n)
    for (v1,v2) in lst:
        case.addEdgeFromTo(v1,v2)
        case.addEdgeFromTo(v2,v1)
    return case

def parse_start():
    n=None
    lst = []
    for (line_number, line) in enumerate(stdin):
        split = line.rstrip('\r\n').split(" ")
        if(line_number == 0):
            n=int(split[0])
            continue
        v1, v2 = int(split[0]), int(split[1])
        lst.append((v1,v2))
    return createCase(n,lst)

def randomCase():
    n = random.randint(3,10)
    lst=[]
    for v1 in range(n):
        for i in range(random.randint(2,n*2)):
            lst.append((v1,random.randint(0,n-1)))
    return createCase(n,lst)

def minCut(case):
    caseCopy = copy.deepcopy(case)
    for i in range(len(caseCopy.nodes)-2):
        caseCopy.concatenate()
    return [str(name) for name in caseCopy.nodes[0].edges]
 
 
def tryCase(case):
    counts = {}
    bestC=minCut(case)
    counts[len(bestC)]=1
    n=len(case.nodes)
    repeats=n*(n-1)*math.log(n)     #math.log = ln
    for i in range(1000):
        newC = minCut(case)
        if (len(newC) in counts):
            counts[len(newC)]+=1
        else:
            counts[len(newC)]=1
        if(len(newC)<len(bestC)):
            bestC = newC
    print("Cut=",bestC)
    print("Number of different sizes of cuts found=",counts)
    print("")

#tryCase(parse_start())
tryCase(createCase(5, [(0, 1), (0,2), (0,3), (1,2), (1,3), (2,3), (2,4), (3,4)]))
tryCase(randomCase())