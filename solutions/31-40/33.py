import math
from fractions import Fraction

def is_canceling(num, den):
    comparison = num/den
    if comparison >= 1 or num%10 == math.floor(num/10) or num%10 ==den%10:
        return False
    if denominator%10 != 0 and math.floor(numerator/10)/(denominator%10) == comparison and numerator%10 == math.floor(denominator/10):
        return True

outnum = 1
outden = 1
for numerator in range(11, 100):
    for denominator in range(numerator, 99):
        if is_canceling(numerator, denominator):
            print("%d/%d" % (numerator,denominator))
            outnum *= numerator
            outden *= denominator
print(Fraction(outnum,outden))