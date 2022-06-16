from sys import stdin
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def randomBoolList(t):
    return [random.randint(0,1)==0 for i in range(t)]

def getVal(vector, i):
    if (i<len(vector)):
        return vector[i]
    return False
def basic(a,b):
    if (len(a) != len(b)):
        print("not same size")
        return
    t = len(a)
    z=[False for i in range(2*t)]
    for i in range(len(z)):
        res=False
        for j in range(i+1):
            v1 = getVal(a,j)
            v2 = getVal(b,i-j)
            res = res or (v1 and  v2)
        z[i]=res
    return z

def toInt(lst,sizeChunks):
    t=len(lst)
    zeroes=""
    for i in range(sizeChunks-1):
        zeroes+="0"
    res=""
    for v in lst:
        res+=str(v+0)
        res+=zeroes
    if(sizeChunks-1>0):
        res=res[0:-(sizeChunks-1)]
    return int(res, 2)

def toBin(v):
    return format(v, "b")

def padWithZeroes(bin_res, sizeChunks,t):
    for i in range(sizeChunks):
        bin_res+="0"
    while(len(bin_res)<2*t*sizeChunks):
        bin_res="0"+bin_res
    return bin_res


def intToResult(prod, sizeChunks, t):
    bin_res=toBin(prod)
    bin_res=padWithZeroes(bin_res,sizeChunks, t)
    res=["1" in bin_res[i:i + sizeChunks] for i in range(0, len(bin_res), sizeChunks)]
    return (bin_res,res)


def intMullReductionMethod1(a,b):
    sizeChunks=1+math.ceil(math.log(len(a),2))
    prod=toInt(a,sizeChunks)*toInt(b,sizeChunks)
    return intToResult(prod, sizeChunks, len(a))



def computePolynomial(a,x):
    powerX=1
    res=0
    for v in a[::-1]:
        res += v*powerX
        powerX*=x
    return res

def intMullReductionMethod2(a,b):
    x=2
    while(x<len(a)+2):
        x*=2
    sizeChunks=1+math.ceil(math.log(len(a),2))
    prod=computePolynomial(a,x)*computePolynomial(b,x)
    return intToResult(prod, sizeChunks, len(a))



def basicTestCase():
    a=[False, False, True, True, False]
    b=[False, False, True, True, False]
    realRes=basic(a,b)
    (bin_res1,reductionRes1)=intMullReductionMethod1(a,b)
    (bin_res2,reductionRes2)=intMullReductionMethod2(a,b)
    print(len(realRes),realRes)
    print(len(reductionRes1),reductionRes1)
    print(len(reductionRes2),reductionRes2)
    print(bin_res1)
    print(bin_res2)

def main():
    for i in range(10000):
        t=random.randint(1,10)
        a=randomBoolList(t)
        b=randomBoolList(t)
        realRes=basic(a,b)
        (bin_res1,reductionRes1)=intMullReductionMethod1(a,b)
        (bin_res2,reductionRes2)=intMullReductionMethod2(a,b)
        if(reductionRes1 != realRes or reductionRes2 != realRes):
            print("a=",a,[v+0 for v in a])
            print("b=",b,[v+0 for v in b])
            print([v+0 for v in realRes])
            print([v+0 for v in reductionRes1])
            print([v+0 for v in reductionRes2])
            break
main()
