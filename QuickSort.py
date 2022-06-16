from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def quickSort(lst):
    if (len(lst) <= 1):
        return (lst,0)
    pivot = lst.pop(random.randint(0, len(lst)-1))
    lst_less=[]
    lst_more=[]
    comp=0
    for i in lst:
        comp+=1
        if (i<pivot):
            lst_less.append(i)
        else:
            lst_more.append(i)
    (res1,com1),(res2,com2) = quickSort(lst_less), quickSort(lst_more)
    return (res1+[pivot]+res2, comp+com1+com2)



def quickSort2(lst,m):
    if (len(lst) <= 1):
        return (lst,m)
    pivot = lst.pop(random.randint(0, len(lst)-1))
    lst_less=[]
    lst_more=[]
    comp=0
    for i in lst:
        m[i][pivot] += 1
        m[pivot][i] += 1
        if (i<pivot):
            lst_less.append(i)
        else:
            lst_more.append(i)
    (res1,m2) = quickSort2(lst_less, m)
    (res2,m3) = quickSort2(lst_more, m2)
    return (res1+[pivot]+res2, m3)

def randomLst():
    return [random.randint(0,999999) for i in range(random.randint(5,50000))]

def sortedList(size):
    return [i for i in range(size)]

def expected(n):
    hn=sum([1/i for i in range(1,n+1)])
    return 2*(n+1)*hn - 4*n

def tryMultipleTimes(times, lst):
    count = 0
    for i in range(times):
        (res1,com1)=quickSort(lst.copy())
        count+=com1
    print(len(lst),"\t", round(count/times,0),"\t",expected(len(lst)))


def countComparisons():
    for i in range(1000):
        tryMultipleTimes(3, randomLst())

def plotComparisonMatrixForSorted():
    n=50
    currSortedList=sortedList(n)
    m=[[0 for i in range(len(currSortedList))] for v in range(len(currSortedList))]
    repeats=100000
    for i in range(repeats):
        (res,m2)=quickSort2(currSortedList.copy(), m)
        m=m2
    for v in m:
        print([k/repeats for k in v])
    print("")
    plt.imshow(m, extent=(0, n, n, 0),
           interpolation='nearest', cmap=cm.gist_rainbow)
    plt.show()


#countComparisons()
plotComparisonMatrixForSorted()

