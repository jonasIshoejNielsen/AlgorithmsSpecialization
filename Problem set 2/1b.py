from sys import stdin
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

ps=[]
cs=[]
points = 10
for i in range(1, points):
    p=i/points
    paren=1-p
    res=1
    count=0
    while(res > 0.01):
        res *= paren
        count +=1
    print("$$","p=",p,", c=",count,"$$")
    ps.append(p)
    cs.append(count)

plt.plot(ps,cs)
plt.show()