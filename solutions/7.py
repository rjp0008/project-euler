import math,sys

#refactored from problem 3
def isPrime(input):
	if(input % 2 == 0):
		return False
	for x in range(2,int(math.sqrt(input)+1)):
		if(input%x == 0):
			return False
	return True

def generatePrimes(limit):
	primes = [2,3,5,7,11,13]
	index = 15
	while(len(primes) < limit):
		if(isPrime(index)):
			primes.append(index)
		#no reason to ever check an even number
		index = index + 2
	return primes[limit-1]
	
print generatePrimes(10001)
