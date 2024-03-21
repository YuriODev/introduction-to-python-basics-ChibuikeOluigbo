# Exercise 8
# Your solution comes here

num = int(input())
num1 = int(input())
num2 = int(input())

max1 = ((num + num1  + abs(num - num1)) // 2) 
max2 = ((num + num1  + abs(num - num1)) // 2) 
max = ((max1 + max2  + abs(max1 - max2)) // 2)
max3 = ((num + num2  + abs(num - num2)) // 2) 
max4 = ((num + num2  + abs(num - num2)) // 2) 
Max = ((max3 + max4  + abs(max3 - max4)) // 2)

Maximum = ((max + Max  + abs(max - Max)) // 2) 

min1 = (abs(abs(num - num1)  - (num + num1)) // 2) 
min2 = (abs(abs(num - num2)  - (num + num2)) // 2)
min = (abs(abs(min1 - min2)  - (min1 + min2)) // 2)
min3 = (abs(abs(num - num2)  - (num + num2)) // 2) 
min4 = (abs(abs(num1 - num2)  - (num1 + num2)) // 2)
Min = (abs(abs(min3 - min4)  - (min3 + min4)) // 2)

Minimum = (abs(abs(min - Min)  - (min + Min)) // 2)

mid = num + num1 + num2 - min - max

print()
print(Minimum)
print(mid)
print(Maximum)