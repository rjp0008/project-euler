from functools import reduce


def sum_num(number):
    return reduce((lambda x, y: int(x) + y), list(map(lambda x: int(x), str(number))))


current_max = 0
for x in reversed(range(0, 100)):
    for y in reversed(range(0, 100)):
        if sum_num(x ** y) > current_max:
            current_max = sum_num(x ** y)

print(current_max)
