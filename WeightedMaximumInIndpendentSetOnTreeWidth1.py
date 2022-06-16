from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

    
class Node(object):
    def __init__(self, v, children):
        self.value = v
        self.children = children
    def printSelf(self,i):
        spaces=""
        for v in range(i):
            spaces+='\t'

        print(spaces,self.value)
        for c in self.children:
            c.printSelf(i+1)

def aux(v):
    sumDrop,sumTake=0, v.value
    for c in v.children:
        childdDrop, childTake=aux(c)
        sumDrop+=max(childTake,childdDrop)
        sumTake+=childdDrop
    #print(v.value,'\t', sumDrop,sumTake)
    return sumDrop,sumTake


example=Node(1, [
    Node(15,[Node(11,[]), Node(11,[])]),
    Node(90,[Node(6,[Node(1,[])]), Node(12,[Node(7,[])]) ])
    ])
example.printSelf(0)

print("res=",max(aux(example)))