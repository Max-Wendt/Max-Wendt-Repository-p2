prime_count = 1
primels = []

def primesieve(x):
    for i in range (2, x - 1):
        if x % i == 0:
            return False
    return True
number = 1
while prime_count <= 10001:
    if primesieve(number) == True:
        prime_count += 1
        primels.append(number)

    number += 2

print (max(primels))
            
                





 
