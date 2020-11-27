
palidromes = []

for x in range (600, 1000):
    for y in range (500, 1000):
        num = x * y
        rev = str(num)
        rev = rev[::-1]
        rev = int(rev)
        if rev == num:
            palidromes.append (num)
        y += 1

    x += 1
print (max(palidromes))
