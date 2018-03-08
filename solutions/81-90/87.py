sq_rt = 7075
cu_rt = 370
fouth_rt = 85

primes = [2]

for x in range(3,sq_rt+1):
    for y in range(2,x+1):
        if y == x:
            primes.append(x)
        if x % y == 0:
            break
sq_rt = primes
cu_rt = list(filter(lambda x: x<cu_rt,primes))
fouth_rt = list(filter(lambda x:x<fouth_rt,cu_rt))

numbers = {}
for x in sq_rt:
    for y in cu_rt:
        for z in fouth_rt:
            if x**2 + y**3 + z**4 <50000000:
                numbers[x**2 + y**3 + z**4] = 1

print(len(numbers))