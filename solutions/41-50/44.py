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

def constraint(x):
    return is_pentegonal(x[0]+x[1])

def constraint(x):
    return is_pentegonal(abs(x[0]-x[1]))

