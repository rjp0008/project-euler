import itertools

def is_lychrel(number,iteration):
    if iteration > 50:
        return True
    if iteration > 0 and str(number) == str(number)[::-1]:
        return False
    return is_lychrel(int(str(number)[::-1])+number,iteration+1)

counter = 0
for x in itertools.count():
    if x > 10000:
        break
    if is_lychrel(x,0):
        counter= counter +1

print(counter)