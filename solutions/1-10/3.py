import math,sys

def largestPrimeFactor(input):
	#for square root of input, to 0 
	for x in reversed(range(int(math.sqrt(input)))):
		#test if divisor
		if input % x == 0:
			if isPrime(x):
				return x
	
def isPrime(input):
	if(input % 2 == 0):
		return False
	for x in range(2,int(math.sqrt(input))):
		if(input%x == 0):
			return False
	return True

try:
	print largestPrimeFactor(int(sys.argv[1]))
except:
	print "Expected a command line argument of type integer."