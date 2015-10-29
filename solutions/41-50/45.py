def Triangle(input):
	return (input * (input + 1)) / 2

def Pentagonal(input):
	return (input * (3 * input - 1)) / 2

def Hexagonal(input):
	return (input * (2 * input - 1))

triangleN = 285
pentagonalN = 165
hexagonalN = 143

while(True):
	triangleN = triangleN + 1
	while Triangle(triangleN) > Pentagonal(pentagonalN):
		pentagonalN = pentagonalN + 1
	while Triangle(triangleN) > Hexagonal(hexagonalN):
		hexagonalN = hexagonalN + 1
	if Triangle(triangleN) == Pentagonal(pentagonalN):
		if Hexagonal(hexagonalN) == Pentagonal(pentagonalN):
			print Triangle(triangleN)
			break