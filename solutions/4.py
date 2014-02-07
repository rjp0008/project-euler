import math,sys

def testIfPalindrome(input):
	string = str(input)
	startingPosition = 0
	endingPosition = len(string) - 1
	
	while startingPosition < endingPosition:
		if(string[startingPosition] != string[endingPosition]):
			return False
		startingPosition = startingPosition + 1
		endingPosition = endingPosition - 1
	return True
	
def largestPalindrome(numberOfDigits):
	largestFound = 0
	currentOutput = (0,0)
	for firstProduct in reversed(range(1,int(math.pow(10,numberOfDigits)))):
		for secondProduct in reversed(range(1,int(math.pow(10,numberOfDigits)))):
			if(testIfPalindrome(firstProduct*secondProduct)):
				if(largestFound < firstProduct*secondProduct):
					currentOutput = (firstProduct,secondProduct)
					largestFound = firstProduct*secondProduct
	return currentOutput, largestFound
	
try:
	print largestPalindrome(int(sys.argv[1]))
except:
	print "Expected a command line argument how many digits the multiplier and multiplicand should be."
	
	