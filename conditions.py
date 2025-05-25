# Write a Python program that checks whether a given number is:

# Even or odd

# Positive, negative, or zero
print("Enter a number to check even, odd or positive, negative or zero:")
number=int(input())

#Here when a number is divisible by 2, it is even and when not divisible, it is odd
if number % 2 == 0:

    print("The number",number, "is even.")
else:
     print("The number",number, "is odd.")
     
     
#if a number is greater than zero, it is positive, if a number is less than zero, it is negative and when equal to zero, it is zero 
if number>0:
    print(number, "is positive.")
elif number<0:
    print(number, "is negative.")
else:
    print(number, "is zero.")
    
#output examples
'''Enter a number to check even, odd or positive, negative or zero:
-5
The number -5 is odd.
-5 is negative.

Enter a number to check even, odd or positive, negative or zero:
5
The number 5 is odd.
5 is positive.

Enter a number to check even, odd or positive, negative or zero:
4
The number 4 is even.
4 is positive.
'''

