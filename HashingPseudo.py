from sys import stdin
import random
import math
import numpy as np
import sympy.ntheory as nt
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def hashSudo(u,n):
    random.seed(u)
    return random.randint(0, n-1)

def getPrimes(n):
    return list(nt.primerange(0, n))[-1]

def convertValueToVectorOfSizeR(u,r,p):
    blockSize=math.floor(math.log2(p))
    print(blockSize,r)
    binaryRep=bin(u)[0]+bin(u)[2:]
    zeroes=""
    for i in range(blockSize*r):
        zeroes+="0"
    binaryRep+=zeroes
    print(binaryRep)
    for i in range(r):
        print("\t",binaryRep[i*blockSize: (i+1)*blockSize])
    return [] #todo
def getR(p,n):
    return math.floor(math.log2(p)/(math.log2(n)))
def getA(r,p):
    return [random.randint(0,p-1) for i in range(r)]

def hash(u,A,p):
    r=len(A)
    xs=convertValueToVectorOfSizeR(u,r,p)
    sum=0
    for i in range(r):
        sum+=A(i)*xs(i)
    return sum % p

def contains(m,n,inserts):
    for u in range(inserts):
        hu=hashSudo(u,n)
        if u not in m[hu]:
            return (False,u)
    return (True, None)
   
p=getPrimes(10)
n=p
m=[[] for i in range(n)]
inserts=10000
for u in range(inserts):
    #hu=hashSudo(u,n)
    r=getR(p,n)
    A=getA(r,p)
    hu=hash(u,A,p)
    m[hu].append(u)

print([len(hu) for hu in m])
print(contains(m,n,inserts))
