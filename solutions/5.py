import math,sys

def findSmallestDivisibility(numberToTestTo):
	index = numberToTestTo*(numberToTestTo-1)
	while(True):
		#anything divisible by 9-20 is divisible by everything smaller than 9
		for x in reversed(range(9,numberToTestTo+1)):
			if(index%x != 0):
				break;
			if(x == 9):
				return index
		#no need to increment by one, when you know the next possible number is going to be a multiple of nTTT and nTTT-1
		index = index + (numberToTestTo*(numberToTestTo-1))
		
print findSmallestDivisibility(20)
	
	