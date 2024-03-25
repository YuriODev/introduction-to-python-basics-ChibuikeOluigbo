# Exercise 11 -> Should be correct
# Your solution comes here

# money = int(input("How much money would you like to withdraw: "))
money = int(input())


c_500 = money // 500
mr = money - (c_500 * 500)

c_100 = mr // 100
mr1 = mr - (c_100 * 100)

c_10 = mr1 // 10
mr2 = mr1 -(c_10 * 10)

c_5 = mr2 // 5
mr3 = mr2 - (c_5 * 5)

c_2 = mr3 // 2
mr4 = mr3 - (c_2 * 2)

c_1 = mr4 // 1
mr5 = mr4 - (c_1 * 1)

print(f"{c_500} : (500), {c_100} : (100), {c_10} : (10), {c_5} : (5), {c_2} : (2), {c_1} : (1)")