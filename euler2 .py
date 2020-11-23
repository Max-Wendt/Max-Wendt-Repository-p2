x = 0
y = 1
sum = 0
while x <= 4000000:
    
    y = x + y 
    x = y - x

    if y % 2 == 0:
        sum += y
print("the sum of even fibonacci numbers under 4000000 is:\n", sum, sep = "")
