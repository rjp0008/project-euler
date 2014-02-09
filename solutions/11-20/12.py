import math,sys

#only check up to square root, because each number under this has a pair above it
def numberOfDivisors(input):
	count = 0
	for x in range(1,int(math.sqrt(input))):
		if(input%x == 0):
			count = count + 1
	if input%int(math.sqrt(input)) == 0:
		return count * 2 - 1
	return count * 2
	
#this is a geometric series of 1+2+3+4+5+6+...+n
def triangleNumber(limit):
	return (limit*(limit+1))/2

def triangleNumberWithMoreThanNDivisors(n):
	answer = 1
	while(True):
		if(numberOfDivisors(triangleNumber(answer)) > n):
			break;
		answer = answer + 1
	return triangleNumber(answer)
	
print triangleNumberWithMoreThanNDivisors(500)
		