import math
dict = {}

a = 100
b = 100

for x in range(2,a +1):
	for y in range(2,b+1):
		dict[int(math.pow(x,y))] = 1
		
print len(dict.keys())