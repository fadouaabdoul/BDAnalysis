import math

#the formula of the probability is P(X=k) = (n choose k)/2n
#(n choose k) = n! / (k! × (n-k)!)

def FlipCoin(n,k):
    nCK = math.comb(n, k)
    pCK = math.pow(2, n)
    P = nCK/pCK
    print(P)

FlipCoin(5,5)