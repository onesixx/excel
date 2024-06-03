import random

a_1 = random.random()
print("a_1 : ", a_1)

a_2 = random.random()
print("a_2 : ", a_2)


import random
import numpy as np

#=== Using random module
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_number = random.randint(1, 100)  # 16
random_float  = random.random()         # 0.5939133088885342
random_float  = random.uniform(1, 100)  # 79.4696745055879
random_number  = random.choice([1, 2, 3, 4, 5])   # 3
random_numbers = random.sample(range(1, 100), k=5)# [16, 4, 10, 5, 1]
random_number  = random.randrange(start=1, stop=100, step=2)      # 57
random.shuffle(numbers)