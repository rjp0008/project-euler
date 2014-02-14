import math,sys

def powerDigitSum(power):
	sumNumber = int(math.pow(2,power))
	numberString = str(sumNumber)
	answer = 0
	for x in range(len(numberString)):
		answer = answer + int(numberString[x])
	return answer
	
print powerDigitSum(1000)