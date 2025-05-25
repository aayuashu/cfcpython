# write a program that takes a string input from the user and performes the following
# prints the string in the reverse
# converts the string to uppercase
# counts the number of vowels in the string

name=str(input("enter you name:"))
#reverse
print(name[::-1])
#upper
print(name.upper())
#vowel
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(1 for ch in name if ch in vowels)

print("Number of vowels:", c)


