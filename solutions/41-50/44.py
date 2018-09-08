import math
from itertools import starmap


def pentagonal_index(pentagonal_num):
    return (1 / 6) * (1 + math.sqrt((24 * pentagonal_num) + 1))


def pentagonal_number(index):
    return (index * (3 * index - 1)) / 2


max_found = 12
low_bound = 1
high_bound = 2
number_map = {0:0,1: 1, 2: 5,3:12}
moving_high = 1
moving_low = 0

while True:
    max_index = max(number_map.keys())
    while number_map[high_bound+moving_high] + number_map[low_bound+moving_low] > max_found:
        max_index += 1
        number_map[max_index] = max_found = int(pentagonal_number(max_index))
    if moving_high > 0:
        if number_map[moving_high] + number_map[low_bound] in number_map.values():
            # if number_map[high_bound] - number_map[low_bound] in number_map.values():
            print(number_map[high_bound] - number_map[low_bound])
            exit(0)
    else:
        if number_map[high_bound] + number_map[moving_low] in number_map.values():
            # if number_map[high_bound] - number_map[low_bound] in number_map.values():
            print(number_map[high_bound] - number_map[low_bound])
            exit(0)

    if number_map[high_bound + 1] - number_map[high_bound-moving_high] <  number_map[low_bound-moving_low] or high_bound <= low_bound + 1:
        if moving_low == 0:
            moving_high += 1
        else:
            moving_high += 1
            low_bound = moving_low
            moving_low = 0
    else:
        if moving_high == 0:
            moving_low += 1
        else:
            moving_low += 1
            high_bound = moving_high
            moving_high = 0