import math

def generate_primelist(end, starter = None):
    if starter == None:
        starter = [2,3,5]
    count = starter[-1]
    while count < end:
        if not any(count % x == 0 for x in starter):
            starter.append(count)
        count += 2
    return starter

def check_composite(check,primes):
    if check in primes or check % 2 == 0:
        return True
    for item in primes:
        close = (check - item) / 2
        if close < 1:
            return True
        close = math.ceil(math.sqrt(close))
        if math.isclose(close,0.0):
            return True
    return False

limit = 10
list = None
while True:
    limit = limit**2
    list = generate_primelist(limit*2,list)
    for item in range(int(math.sqrt(limit))+1,limit,2):
        if not check_composite(item,list):
            print(item)