import math,sys

def isTriplet(a,b,c):
	if(a<b):
		return int(math.pow(a,2)) + int(math.pow(b,2)) == int(math.pow(c,2))

a = 0
b = 0
c = 1000
for x in range(1000):
	for y in range(1000):
		a = 1000 - y
		b = 1000 - x
		c = 1000 - a - b
		if(isTriplet(a,b,c)):
			print a*b*c			