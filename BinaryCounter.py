from sys import stdin
from typing import Counter


def increment(counter):
    for i in range(len(counter)):
        if(counter[i]==0):
            counter[i] = 1
            return True
        if(i==len(counter)-1):
            return False
        counter[i]=0
    
def binaryCounter(n, function):
    counter=[]
    for i in range(n):
        counter.append(0)
    while(increment(counter)):
        print(counter)
        function(counter)
    
    print("done")
        

func = lambda counter: print(sum(counter))
binaryCounter(n=4, function=func)
