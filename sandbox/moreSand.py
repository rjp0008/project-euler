#quick refactoring from problem 2

FirstNumber = 1
SecondNumber = 2
SumOfEvenNumbers = 0
UPPER_LIMIT = 4000000
counter = 3

#change the conditional to check for 1000 digits
while len(str(SecondNumber)) < 1000:
#while SecondNumber < UPPER_LIMIT:
	counter = counter + 1
	temp = SecondNumber
	SecondNumber = FirstNumber + SecondNumber
	FirstNumber = temp
print counter
	