import itertools

total_number = 0
for x in range(1,10):
    too_far = False
    for y in itertools.count(1):
        if len(str(x**y)) == y:
            too_far = True
            total_number += 1
        if len(str(x**y)) < y and too_far:
            break

print(total_number)
