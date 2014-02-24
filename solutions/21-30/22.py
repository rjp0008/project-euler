def readNames():
	names = []
	file = open('names.txt','r')
	for line in file:
		names = (line.split("\",\""))
	return names
	
	
def nameScore(listOfNames):
	output = 0
	for x in range(1,len(listOfNames)+1):
		intermediate = 0
		for y in range(len(listOfNames[x-1])):
			intermediate = intermediate + ord(listOfNames[x-1][y]) - 64
		output = output + intermediate*x
	return output
	
nameList = readNames()
nameList.sort()
print nameScore(nameList)