FirstNumber = 1
SecondNumber = 2
SumOfEvenNumbers = 0
UPPER_LIMIT = 4000000
while SecondNumber < UPPER_LIMIT:
	if(SecondNumber%2 == 0):
		SumOfEvenNumbers = SecondNumber + SumOfEvenNumbers
	temp = SecondNumber
	SecondNumber = FirstNumber + SecondNumber
	FirstNumber = temp
print SumOfEvenNumbers
	