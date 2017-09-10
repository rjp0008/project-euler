import itertools
products = []
for item in itertools.permutations('123456789', 9):
    for x in range(1,7):
        for y in range(x+1,7):
            i = "".join(item[:x])
            j = "".join(item[x:y])
            k = "".join(item[y:])
            if int(i)*int(j) == int(k):
                if int(k) not in products:
                    products.append(int(k))
print(sum(products))