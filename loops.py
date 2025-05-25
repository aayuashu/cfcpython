#Write a python program that prints all numbers from 1 to 100 that are divisible by 3 but not divisible by 5

for i in range(1, 100):
    if i%3== 0 and i%5 != 0:
        print(i)
        
#outputs

# 3
# 6
# 9
# 12
# 18
# 21
# 24
# 27
# 33
# 36
# 39
# 42
# 48
# 51
# 54
# 57
# 63
# 66
# 69
# 72
# 78
# 81
# 84
# 87
# 93
# 96
# 99