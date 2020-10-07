
# trues = results.count(True)
# falses = results.count(False)
# print(f"Probability of forming triangle: {trues/(trues+falses)}")

# end = time.time()
# print('Time = ', end - start)
    
    
import time
start = time.time()

import numpy as np

samples = 10000000
break_points = np.random.uniform(0, 1, (2, samples))
piece_one = np.minimum(*break_points)
piece_two = np.maximum(*break_points) - piece_one
piece_three = 1 - (piece_one + piece_two)
cond1 = piece_one + piece_two > piece_three
cond2 = piece_two + piece_three > piece_one
cond3 = piece_three + piece_one > piece_two
probability = sum(cond1 & cond2 & cond3)/samples

print(probability)

end = time.time()

print('Time = ', end - start)

def create_list():
    x=0
    lista = []
    while True:
        lista.append(x)
        x+= 0.01
        if x > 1:
            break
    return lista
create_list()