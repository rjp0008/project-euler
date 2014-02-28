import math

def isPrime(input):
	if(input % 2 == 0 or input == 1):
		return False
	for x in range(2,int(math.sqrt(input)+1)):
		if(input%x == 0):
			return False
	return True
	
def isTruncatablePrime(input):
	if not (isPrime(input)):
		return False
	length = len(str(input))
	digits = []
	for x in str(input):
		digits.append(int(x))
	digits.pop(0)
	while(len(digits) > 0):
		count = 0
		tempNum = 0
		while len(temp) > 0:
			tempNum += int(digits.pop()) * (math.pow(10,count))
			count += 1
		if not (isPrime(tempNum)):
			return False
	for x in str(input):
		digits.append(int(x))
	while(len(digits) > 0):
		count = 0
		tempNum = 0
		while len(temp) > 0:
			tempNum += int(temp.pop()) * (math.pow(10,count))
			count += 1
		if not (isPrime(tempNum)):
			return False
	return True
		
primes = []
counter = 10
sum = 0
while len(primes) < 11:
	if(isTruncatablePrime(counter)):
		primes.append(counter)
		sum += counter
		print counter
	counter += 1

print sum