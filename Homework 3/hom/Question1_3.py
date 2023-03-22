
from collections import Counter
import copy
import numpy as np
from Qestion1_1 import random_list
from Question1_2 import computer
def scale(a):
    max = np.max(a)
    min = np.min(a)

    for i in range(len(a)):
        a[i] = int((a[i] - min)/(max-min)*9)
    print((Counter(a)))
    return a

a = random_list(100)
b = random_list(125)
c = random_list(150)

a1 = scale(copy.copy(a))
print(str(a)+ ' -> '+ str(a1))
computer(a1)

b1 = scale(copy.copy(b))
print(str(b)+ ' -> ' +str(b1))
computer(b1)

c1 = scale(copy.copy(c))
print(str(c)+ ' -> ' +str(c1))
computer(c1)
