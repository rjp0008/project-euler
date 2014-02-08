import math,sys

#using reference from http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#sadly this is broken, most likely culprit is an off by one error on indexes
def listOfPrimes(limit):
	primes = []
	finalList = []
	for _ in range(limit):
		primes.append(True)
	primes[0] = False
	for i in range(2,int(math.sqrt(limit))):
		if primes[i] == True:
			for j in range(int(math.pow(i,2)),limit,i):
				if(j < limit):
					primes[j-1] = False
	for x in range(0,len(primes)-1):
		if primes[x] == True:
			print x+1
			finalList.append(x+1)
	return finalList

#refactored from problem 3
def isPrime(input):
	if(input % 2 == 0):
		return False
	for x in range(2,int(math.sqrt(input)+1)):
		if(input%x == 0):
			return False
	return True
				
				
total = 0
for x in range(3,2000000):
	if(isPrime(x)):
		print x
		total = total + x
#add two to account for isPrime() function not finding 2 as a prime
print total +2