import math,sys

def sumOfSquares(limit):
	runningTotal = 0
	for x in range(limit+1):
		runningTotal = math.pow(x,2) + runningTotal
	return int(runningTotal)
	
def squareOfSums(limit):
	#sum of the form 1+2+3+4+...+n = (n(n+1))/2
	return int(math.pow((limit*(limit+1)/2),2))
		
print squareOfSums(100)-sumOfSquares(100)