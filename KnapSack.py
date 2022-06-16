from sys import stdin
import math
import random

class Case(object):
    def __init__(self, capacity):
        self.lst = []
        self.capacity=capacity
    
    def setList(self, lst):
        self.lst=lst
    def addToLst(self, item):
        self.lst.append(item)
    
    def sortList(self):
        self.lst.sort(key=lambda e: e)


def randomCase(max_n, max_weights, max_profit):
    lst=[(random.randint(1,max_weights), random.randint(1,max_profit)) for i in range(random.randint(3,max_n))]
    B=random.randint(5, max_weights*len(lst))
    case = Case(B)
    case.setList(lst)
    return case

def normalKnapsack(case):
    case.sortList();
    OPT=[[0 for i in range(case.capacity+1)] for v in range(len(case.lst)+1)]
    i=0
    for (w,p) in case.lst:
        i+=1
        for j in range(len(OPT[0])):
            if (w>j):
                OPT[i][j]=OPT[i-1][j]
                continue
            OPT[i][j]=max(OPT[i-1][j], OPT[i-1][j-w]+p)
    return OPT[i][-1]

def n2p_Knapsack(case):
    case.sortList();
    p=max(case.lst, key=lambda x:x[1])[1]
    OPT=[[-1 for i in range(p*len(case.lst))] for v in range(len(case.lst)+1)]
    i=0
    for (wi,pi) in case.lst:
        i+=1
        for p in range(len(OPT[0])):
            if(pi>p):
                OPT[i][p]=OPT[i-1][p]
                continue
            if (OPT[i-1][p-pi]==-1 and p-pi!=0):
                OPT[i][p]=OPT[i-1][p]
                continue
            if(OPT[i-1][p]==-1):
                OPT[i][p]=max(0,OPT[i-1][p-pi])+wi
                continue
            OPT[i][p]=min(OPT[i-1][p], max(0,OPT[i-1][p-pi])+wi)
    best=0
    for v in range(len(OPT[i])):
        if(OPT[i][v]!=-1 and OPT[i][v]<=case.capacity):
            best=v
    return (best,OPT)

def workBack(OPT, res, case):
    curr=res
    indexes=[]
    for i in range(len(OPT)-1, 0, -1):
        if(OPT[i-1][curr]!=-1):
            continue
        indexes.append(i-1)
        curr-=case.lst[i-1][1]
    return indexes
            

def n3_Knapsack_approx(case, epsilon):
    p=max(case.lst, key=lambda x:x[1])[1]
    K=float(epsilon)*float(p)/len(case.lst)
    print(K, p, math.floor(p/K))
    oldList=case.lst
    newList=[(math.floor(pi/K), w) for (pi,w) in case.lst]
    case.lst=newList
    (res, OPT) = n2p_Knapsack(case)
    case.lst=oldList
    return (sum([case.lst[i][1] for i in workBack(OPT, res, case)]), OPT)

tests=100
for t in range(tests):
    case = randomCase(30, 30, 30)
    res1 = normalKnapsack(case)
    (res2,_) = n2p_Knapsack(case)
    epsilon=0.01
    (res3,_) = n3_Knapsack_approx(case, 2)
    if(res1 != res2):
        print("Error=n2p_Knapsack")
        print(case.lst)
        print(case.capacity)
        print("")
        print(res1,"=normalKnapsack")
        print(res2,"=n2p_Knapsack")
        break
    if(res3<(1-epsilon)*res2):
        print(res2, "approximately",res3)

"""
case = randomCase(10, 10, 10)
case.lst=[(1, 4), (5, 8), (7, 9), (8, 10), (9, 7)]
case.capacity=7
(res2,OPT) = n2p_Knapsack(case)
print(res2)
for op in OPT:
    print(op)

workBack(OPT, res2, case)
"""