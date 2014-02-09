import math,sys

#working on problem 11, just looking at the grid and thinking of implementation/strategy
#I decided to guess four numbers, it was the right answer (70600674)
#This is the solution I came up with though, it's packaged with a text file of numbers in a space
#delimited grid


def initGrid():
	grid = []
	file = open('numberGrid.txt','r')
	for x in range(20):
		data = file.readline()
		line = []
		for y in range(20):
			line.append(int(data.split(" ")[y]))
		grid.append(line)
	return grid
	
def findMaxProduct(grid,x,y):
	max = 0
	if(x>=3 and x <=16):
		if(grid[y][x-3]*grid[y][x-2]*grid[y][x-1]*grid[y][x] > max):
			max = grid[y][x-3]*grid[y][x-2]*grid[y][x-1]*grid[y][x]
		if(grid[y][x+3]*grid[y][x+2]*grid[y][x+1]*grid[y][x] > max):
			max = grid[y][x-3]*grid[y][x-2]*grid[y][x-1]*grid[y][x]
	if(y>=3 and y <=16):
		if(grid[y-3][x]*grid[y-2][x]*grid[y-1][x]*grid[y][x] > max):
			max = grid[y-3][x]*grid[y-2][x]*grid[y-1][x]*grid[y][x]
		if(grid[y+3][x]*grid[y+2][x]*grid[y+1][x]*grid[y][x] > max):
			max = grid[y-3][x]*grid[y-2][x]*grid[y-1][x]*grid[y][x]
	if y>=3 and y <=16 and x>=3 and x <=16:
		if(grid[y-3][x-3]*grid[y-2][x-2]*grid[y-1][x-1]*grid[y][x] > max):
			max = grid[y-3][x-3]*grid[y-2][x-2]*grid[y-1][x-1]*grid[y][x]
		if(grid[y+3][x+3]*grid[y+2][x+2]*grid[y+1][x+1]*grid[y][x] > max):
			max = grid[y-3][x+3]*grid[y-2][x+2]*grid[y-1][x+1]*grid[y][x]
		if(grid[y-3][x+3]*grid[y-2][x+2]*grid[y-1][x+1]*grid[y][x] > max):
			max = grid[y-3][x+3]*grid[y-2][x+2]*grid[y-1][x+1]*grid[y][x]
		if(grid[y+3][x-3]*grid[y+2][x-2]*grid[y+1][x-1]*grid[y][x] > max):
			max = grid[y+3][x-3]*grid[y+2][x-2]*grid[y+1][x-1]*grid[y][x]
	return max
		
	
output = 0
gridData = initGrid()
for x in range(20):
	for y in range(20):
		if(findMaxProduct(gridData,x,y)>output):
			output = findMaxProduct(gridData,x,y)
				
print output
		
			
		