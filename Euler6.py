def sumsqls(sum):
    sum = 0
    for i in range (0, 101):
        sum += i**2
    return sum

def sqsumls(sum):
    sum = 0
    for i in range (0, 101):
        sum += i
    return sum**2

s1 = sumsqls(sum)
s2 = sqsumls(sum)

print ("Differnce of squares of sum and sum of squares is up to 100 is: " + str(s2 - s1))
    
        
    
