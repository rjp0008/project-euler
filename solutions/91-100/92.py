def hits_89(number):
    if number == 89:
        return True
    if number == 1:
        return False
    return hits_89(sum(list(map(lambda x: int(x)**2, str(number)))))

counter = 0
for x in range(1,10_000_001):
    if hits_89(x):
        counter += 1
print(counter)
