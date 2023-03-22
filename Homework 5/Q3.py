import random  
import numpy
p_fair = 0.5 # probability of heads for fair coin
p_loaded = 0.9 # probability of heads for loaded coin
p_mixed = 0.9 # probability of drawing a fair coin
p_loaded_mixed = 1 - p_mixed # probability of drawing a loaded coin

# probability of getting 5 heads in a row for fair coin
p_five_heads_fair = p_fair ** 5

# probability of getting 5 heads in a row for loaded coin
p_five_heads_loaded = p_loaded ** 5

# probability of getting 5 heads in a row for a randomly drawn coin
p_five_heads_mixed = p_five_heads_fair * p_mixed + p_five_heads_loaded * p_loaded_mixed

print( p_five_heads_mixed)