import math,sys

#there is a library made for this in python
#i used it for a twitter bot I made

CONST_ONE = "one"
CONST_TWO = "two"
CONST_THREE = "three"
CONST_FOUR = "four"
CONST_FIVE = "five"
CONST_SIX = "six"
CONST_SEVEN = "seven"
CONST_EIGHT = "eight"
CONST_NINE = "nine"

CONST_HUND = "hundred"
CONST_THOUSAND = "thousand"

CONST_TEN = "ten"
CONST_TWENTY = "twenty"
CONST_THIRTY = "thirty"
CONST_FOURTY = "forty"
CONST_FIFTY = "fifty"
CONST_SIXTY = "sixty"
CONST_SEVENTY = "seventy"
CONST_EIGHTY = "eighty"
CONST_NINETY = "ninety"

CONST_AND = "and"

defNumberLetterCounts(input):
	output = 0
	if(input>999 and input <= 9999):
		switch str(input)[0]:
			case 1:
				#one thousand
				output = output +  len(CONST_ONE) + len(CONST_THOUSAND)
	elif(input>99):
		#hundreds
		switch str(input)[0]:
			case 1:
				output = output + len(CONST_ONE) + len(CONST_HUND)
			case 2:
				output = output + len(CONST_TWO) + len(CONST_HUND)
			case 3:
				output = output + len(CONST_THREE) + len(CONST_HUND)
			case 4:
				output = output + len(CONST_FOUR) + len(CONST_HUND)
			case 5:
				output = output + len(CONST_FIVE) + len(CONST_HUND)
			case 6:
				output = output + len(CONST_SIX) + len(CONST_HUND)
			case 7:
				output = output + len(CONST_SEVEN) + len(CONST_HUND)
			case 8:
				output = output + len(CONST_EIGHT) + len(CONST_HUND)
			case 9:
				output = output + len(CONST_NINE) + len(CONST_HUND)
	if(str(input)[len(str(input))-2]) > 0):
		#tens
		switch str(input)[len(str(input))-2]:
			case 1:
				output = output + len(CONST_TEN)
	
	str(input)[len(str(input))-1] > 0):
		if
			
			