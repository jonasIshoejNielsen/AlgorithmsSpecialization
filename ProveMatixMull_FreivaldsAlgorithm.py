from sys import stdin
import random
import numpy as np



def determinant(t):
    return np.linalg.det(np.array(t) )

def matrixMultiply(A,B):
    return np.array(A).dot(np.array(B))

def getRandomMatrix(n):
    return [[random.randint(-100, 100) for v in range(n)] for v in range(n)]

def getRandomVector(n):
    res = [random.randint(0, 1) for v in range(n)]
    if (sum(res)==0):
        return getRandomVector(n)
    return res

def equalVectors(v1,v2):
    n=len(v1)
    for r in range(n):
        if(v1[r] != v2[r]):
            return False
    return True


def check(A,B,C):
    n = len(A)
    v = getRandomVector(n)
    v2=matrixMultiply(B,v)
    v3=matrixMultiply(A,v2)
    w=matrixMultiply(C,v)
    
    return (equalVectors(v3,w), A,B,C,v)

def findWhereNoFlasePositive(count):
    n = random.randint(1, 5)
    A=getRandomMatrix(n)
    B=getRandomMatrix(n)
    C=getRandomMatrix(n)
    for i in range(count):
        (res, A,B,C,v) = check(A,B,C)
        if(res):
            return False
    if(str(matrixMultiply(A,B)) == str(C)):
        return False
    print(A)
    print(B)
    print(C)
    print(matrixMultiply(A,B))
    return True

for i in range(1000):
    if (findWhereNoFlasePositive(1000)):
        print(i)
        break
