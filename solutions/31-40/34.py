import math

output = 0
#arbitrarily chose this high number, not sure how to calculate upper bound?
for x in range(3,50000):
	sum = 0
	for digit in str(x):
		sum += math.factorial(int(digit))
	if(x == sum):
		output += x
		print x
print output