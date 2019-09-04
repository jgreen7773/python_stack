# 1
import random
def randint(min='', max=''):
    num = random.random() * min + max
    round(num)
    return num

print(randint(50,500))