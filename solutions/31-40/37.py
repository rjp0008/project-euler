import math

def isPrime(input):
	if input is 2:
		return True
	if(input % 2 is 0):
		return False
	for x in range(3,int(math.sqrt(input))+1,2):
		if(input%x == 0):
			return False
	if input is 1:
		return False
	return True
	
def isTruncatablePrime(number):
	if not isPrime(number):
		return False
	removeLeft = int((str(number))[1:])
	while True:
		if not isPrime(int(removeLeft)):
			return False
		removeLeft = (str(removeLeft))[1:]
		if removeLeft is '':
			break
	removeRight = int((str(number))[:-1])
	while True:
		if not isPrime(int(removeRight)):
			return False
		removeRight = str(removeRight)[:-1]
		if removeRight is '':
			break
	return True
	
list = []
testNumber = 11
while len(list) < 11:
	if isTruncatablePrime(testNumber):
		list.append(testNumber)
		print testNumber
	testNumber += 2
total = 0
for x in list:
	total += x
print total
	
	
