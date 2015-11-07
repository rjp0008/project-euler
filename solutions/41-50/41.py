import itertools
import math

def is_prime(input):
	if input is 2:
		return True
	if(input % 2 is 0):
		return False
	for x in range(3,int(math.sqrt(input)) + 1,2):
		if(input % x == 0):
			return False
	if input is 1:
		return False
	return True

numbers = []
n = 5
largest = 2143
foundPandigital = True
while foundPandigital:
	for x in range(1,n + 1):
		numbers.append(x)
	for permutation in itertools.permutations(numbers):
		place = 1
		temp = 0
		for number in permutation:
			temp = temp + number * place
			place = place * 10
		if is_prime(temp):
			if temp > largest:
				largest = temp
				print largest
	numbers = []
	n = n + 1

