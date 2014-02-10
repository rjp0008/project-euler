import math,sys,time

#from stack overflow for performance measuring
current_milli_time = lambda: int(round(time.time() * 1000))

#this stores and updates the dictionary, though it doesn't gain anything from this
#its just formatted this way to be modular with the recusion approach
def collatzLength(input,dictionary):
	try:
		return dictionary[input],dictionary
	except:
		collatz = input
		counter = 1
		while(collatz != 1):
			if(collatz%2 == 0):
				collatz = collatz/2
			else:
				collatz = (3*collatz) + 1
			counter = counter + 1
		dictionary[input] = counter
		return counter,dictionary
		
#recursiveFunction, also stores the already computed lengths in the dictionary
#so the same things aren't computed multiple times		
def recusionSolution(input,dictionary):
	try:
		return dictionary[input],dictionary
	except:
		currentLength = 0
		couple = 0
		if(input%2 == 0):
			couple = recusionSolution(input/2,dictionary)
			currentLength = 1 + couple[0]
		else:
			couple = recusionSolution(3*input+1,dictionary)
			currentLength = 1 + couple[0]
		couple[1][input] = currentLength
		return currentLength,couple[1]
		
def longestChainUnderNIterative(n,method):
	longestTotal = 0
	theNumber = 0
	collatzInit = {}
	collatzInit[1] = 1
	for x in range(1,n):
		couple = 0
		if method:
			couple = collatzLength(x,collatzInit)
		else:
			couple = recusionSolution(x,collatzInit)
		thisLength = couple[0]
		collatzInit = couple[1]
		if(thisLength > longestTotal):
			longestTotal = thisLength
			theNumber = x
	return longestTotal,theNumber
	
	
#recusion is 6 times faster than iteration
start = current_milli_time()
output = longestChainUnderNIterative(1000000,True)
stop = current_milli_time()
print str((stop - start)/1000.0) + " seconds to compute iterative approach"
print output
start = current_milli_time()
output = longestChainUnderNIterative(1000000,False)
stop = current_milli_time()
print str((stop - start)/1000.0)  +" seconds to compute recursive approach"
print output
