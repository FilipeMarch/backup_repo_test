import time
import secrets
import random
# start = time.time()


def create_list():
    lista = [i/100 for i in range(1001)]
    return lista


def select_two_numbers():
    lista = create_list()[1:-1]
    first_number = secrets.choice(lista)
    lista.remove(first_number)
    second_number = secrets.choice(lista)
    lista = [first_number, second_number]
    lista.sort()    
    return lista[0], lista[1] - lista[0]


def probability_of_something():
    #If I had a stick and I just hit it in two different places, what's the probability the resulting sticks would form a triangle?
    a, b = select_two_numbers()
    c = 10-(a+b)

    a = round(a,2)
    b = round(b,2)
    c = round(c,2)
    
    # print('a = ', a, 'b = ', b, 'c = ', c)
    # print('a+b = ', round(a+b, 2), '> ', c)
    # print('a+c = ', round(a+c, 2), '> ', b)
    # print('b+c = ', round(b+c, 2), '> ', a)

    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

results = [] 
for i in range(100000):
    answer = probability_of_something()
    # print(answer)
    results.append(answer)

    trues = results.count(True)
    falses = results.count(False)
    print(f"Probability of forming triangle: {trues/(trues+falses)}")


# trues = results.count(True)
# falses = results.count(False)
# print(f"Probability of forming triangle: {trues/(trues+falses)}")

# end = time.time()
# print('Time = ', end - start)
    
    

# start = time.time()

# import numpy as np

# samples = 10000000
# break_points = np.random.uniform(0, 1, (2, samples))
# piece_one = np.minimum(*break_points)
# piece_two = np.maximum(*break_points) - piece_one
# piece_three = 1 - (piece_one + piece_two)
# cond1 = piece_one + piece_two > piece_three
# cond2 = piece_two + piece_three > piece_one
# cond3 = piece_three + piece_one > piece_two
# probability = sum(cond1 & cond2 & cond3)/samples

# print(probability)

# end = time.time()

# print('Time = ', end - start)

# def create_list():
#     x=0
#     lista = []
#     while True:
#         lista.append(x)
#         x+= 0.01
#         if x > 1:
#             break
#     return lista
# create_list()