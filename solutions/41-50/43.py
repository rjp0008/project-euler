import itertools
numbers = []
for item in itertools.permutations('1234567890', 10):
    if int("".join(item[1:4])) % 2 != 0:
        continue
    if int("".join(item[2:5])) % 3 != 0:
        continue
    if int("".join(item[3:6])) % 5 != 0:
        continue
    if int("".join(item[4:7])) % 7 != 0:
        continue
    if int("".join(item[5:8])) % 11 != 0:
        continue
    if int("".join(item[6:9])) % 13 != 0:
        continue
    if int("".join(item[7:])) % 17 != 0:
        continue
    numbers.append(int("".join(item)))
print(sum(numbers))