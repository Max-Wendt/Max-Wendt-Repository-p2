primelist = []
n = 1

def primseive(n):
    for i in range (2, n - 1):
        if n % i == 0:
<<<<<<< HEAD
            return False
=======
          return False
>>>>>>> daae5ae1042056ac2965e5b05695d9d3a7b62d78
        return True
        
while n <= 775146:
    n += 1
    if 600851475143 % n == 0:
         if n % 2 != 0:
             if primseive(n) == True:
                 primelist.append(n)

print(max(primelist))
