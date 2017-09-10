import math

def number_combinations(n,r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

counter = 0
for x in range(0,101):
    for y in range(0,x):
        if number_combinations(x,y) > 1000000:
            counter = counter + 1

print(counter)