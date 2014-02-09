import math,sys

#this was super easy in python as there is no upper int limit
def initNumbers():
	numbers = []
	file = open('numbers13.txt','r')
	for x in range(100):
		numbers.append(int(file.readline()))
	return numbers
	
def addNumbers(numList):
	output = 0
	for x in range(len(numList)):
		output = output + numList[x]
	return output
	
def firstTenDigits(input):
	return str(input)[0:10]
	
numbers = initNumbers()
bigAnswer = addNumbers(numbers)
print firstTenDigits(bigAnswer)