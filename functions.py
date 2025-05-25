#Write a function named is_prime(n) that checks whether the given number is a prime number. then ask the user to input three numbers and use the function to check each
n1=int(input("enter first num:"))
n2=int(input("enter second num:"))
n3=int(input("enter third num:"))

import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(n1):
    print(f"{n1} is a prime number")
else:
    print(f"{n1} is not a prime number")
    
if is_prime(n2):
    print(f"{n2} is a prime number")
else:
    print(f"{n2} is not a prime number")
    
if is_prime(n3):
    print(f"{n3} is a prime number")
else:
    print(f"{n3} is not a prime number")