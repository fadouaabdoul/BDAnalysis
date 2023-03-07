import math
def funcos(eps, x): 
    t1 = 1 
    t2 = 2
    y = 1 
    z = 2 
    while(math.fabs(t1) > eps):
        t2 += t1 
        t1 = (-1) * t1 * x * x / y / z
        y += 2 
        z += 2

    t2 += t1 
    print(t2)
eps = float(input('enter eps: '))
x = float(input('enter x:' ))
funcos(eps, x)