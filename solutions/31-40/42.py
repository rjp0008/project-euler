#only works on uppercase values, like the provided txt file
def char_as_int_value(char):
    return ord(char) - 64

#returns true if a number is a triangle number
#triangle numbers follow the pattern 1,3,6,10,15,21,28
# t(n) = n/2(n+1)
def is_triangle_number(number):
    trianglePosition = 0
    while True:
        trianglePosition = trianglePosition + 1
        test = (trianglePosition * .5) * (trianglePosition + 1)
        if test > number:
            return False
        if test == number:
            return True

#read the provided words
with open("p042_words.txt") as f:
    line = f.readlines()
wordlist = line[0].replace("\"","").split(",")

triangleWordCounter = 0
for word in wordlist:
    test = 0
    #split the word into individual characters
    for letter in list(word):
        #add the value of this character to the running total for the word
        test = char_as_int_value(letter) + test
    if is_triangle_number(test):
        triangleWordCounter = triangleWordCounter + 1
print triangleWordCounter