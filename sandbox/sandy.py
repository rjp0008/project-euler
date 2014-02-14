import math,sys,time

paths = 0
#drop the right most column down all the way add one for each time

#when reached the bottom drop the 2nd to last right most column one and repeat above

matrix = [[1 for x in range(2)] for y in range(2)]

def makepath(matrix,runningTotal):
	xPos = 0
	yPos = 0
	for y in range(len(matrix[0])):
		if matrix[y][0] == 1:
			for x in range(len(matrix[0])):
				if matrix[y][x] == 1:
					paths = paths + 
		
