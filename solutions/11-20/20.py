import sys

def N(number):
	if(number == 1):
		return 1
	return number * N(number-1)
	
def sumOfDigits(number):
	numberString = str(number)
	output = 0
	for x in range(len(numberString)):
		output = output + int(numberString[x])
	return output

print sumOfDigits(N(100))