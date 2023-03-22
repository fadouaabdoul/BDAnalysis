import random
import numpy
import math

p_loaded = 0.1 # probability of picking a loaded coin
p_fair = 0.9 # probability of picking a fair coin
n = 10 # number of coin tosses
k = 9 # number of heads

# probability of getting exactly k heads in n tosses for fair coin
p_k_heads_fair = (math.comb(n, k) * 0.5**k * 0.5**(n-k)) 
p_k_heads_fair