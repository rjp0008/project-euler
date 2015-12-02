import itertools
import math

def is_prime(input):
	if input is 2:
		return True
	if(input % 2 is 0):
		return False
	for x in range(3,int(math.sqrt(input)) + 1,2):
		if(input % x == 0):
			return False
	if input is 1:
		return False
	return True

def is_permutation(first,second):
    string1 = str(first)
    string2 = str(second)
    for x in range(0,4):
        string2 = string2.replace(string1[x],"",1)
    return string2 == ""


primes = []
for x in range(1000,10000):
    if is_prime(x):
        primes.append(x)

for i in range(0,len(primes)):
    try:
        if is_permutation(primes[i],primes[primes.index(primes[i]+3330)]):
           if is_permutation(primes[i],primes[primes.index(primes[i]+6660)]):
               print str(primes[i])+str(primes[primes.index(primes[i]+3330)]) +str(primes[primes.index(primes[i]+6660)])
    except:
        #primes.index(int) will fail and come here if the number is not in the list
        pass
