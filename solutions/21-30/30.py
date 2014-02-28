import math
output = 0
for x in range(2,296000):
	sum = 0
	for digit in str(x):
		sum = sum + int(math.pow(float(digit),5.0))
	if(sum == x):
		output += x
print output
	