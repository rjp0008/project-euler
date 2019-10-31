import math
from itertools import starmap
from scipy.optimize import minimize


def pentagonal_index(pentagonal_num):
    return (1 / 6) * (1 + math.sqrt((24 * pentagonal_num) + 1))

def is_pentegonal(num):
    return pentagonal_index(num).is_integer()

def pentagonal_number(index):
    return (index * (3 * index - 1)) / 2

def optimize(x):
    return abs(pentagonal_number(x[0])-pentagonal_number(x[1]))

def constraintsum(x):
    if is_pentegonal(x[0]+x[1]):
        return 0
    return 1

def constraintdiff(x):
    if is_pentegonal(abs(x[0]-x[1])):
        if x[0] >0 and x[1]>0:
            return 0
    return 1

def constraint_pos(x):
    if x[1]>0 and x[0]>0:
        return 0
    return 1

sum = {'type': 'eq', 'fun': constraintsum}
diff = {'type': 'eq', 'fun': constraintdiff}
pos = {'type': 'eq', 'fun': constraint_pos}
x = [1, 5]
solution = minimize(optimize, x, method='SLSQP', constraints=[sum, diff])

print(solution)