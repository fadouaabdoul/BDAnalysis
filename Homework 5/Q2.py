import random

def toss_coin(p):
    return 'heads' if random.random() < p else 'tails'

def five_heads_in_a_row():
    count = 0
    for i in range(100000):
        coin = 'fair' if random.random() < 0.9 else 'loaded'
        result = ''
        if coin == 'fair':
            p = 0.5
        else:
            p = 0.9
        for j in range(5):
            result += toss_coin(p)
        if result == 'heads'*5:
            count += 1
    return count/100000

print(five_heads_in_a_row())