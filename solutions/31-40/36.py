def binaryDecimalPalindrome(number):
	if(decimalPalindrome(number) and binaryPalindrome(number)):
		return True
	return False

def decimalPalindrome(number):
	temp = []
	number_string = str(number)
	for x in number_string:
		temp.append(int(x))
	counter = len(temp)
	for x in range(len(temp)):
		counter -= 1
		if(x>=(len(temp)+1)/2.0):
			break
		if(temp[x] != temp[counter]):
			return False
	return True
	
	
def binaryPalindrome(number):
	temp = []
	while number:
		if(number & 1):
			temp.insert(0,1)
		else:
			temp.insert(0,0)
		number = number >> 1
	counter = len(temp)
	for x in range(len(temp)):
		counter -= 1
		if(x>=(len(temp)+1)/2.0):
			break
		if(temp[x] != temp[counter]):
			return False
	return True
	
	
output = 0
for x in range(1000000):
	if(binaryDecimalPalindrome(x)):
		print x
		output += x
print output

	