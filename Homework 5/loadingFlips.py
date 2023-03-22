import random

def toss_coin():
    return random.choice(['heads', 'tails'])

def five_heads_in_a_row():
    count = 0
    for i in range(100000):
        result = ''
        for j in range(5):
            result += toss_coin()
        if result == 'heads' * 5:
            count += 1
    return count/100000;


print(five_heads_in_a_row())