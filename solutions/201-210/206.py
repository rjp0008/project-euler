compareNumber = "1_2_3_4_5_6_7_8_9_0"

def number_matches(input):
    testString = str(input)
    for x in range(19):
        if compareNumber[x] != "_":
            if compareNumber[x] != testString[x]:
                return False
    return True


numberToTest = 1000000000
found = False
while not(found):
    if number_matches(numberToTest*numberToTest):
        found = True
    #number has to end in 0 so add another 10
    numberToTest = numberToTest + 10
print numberToTest