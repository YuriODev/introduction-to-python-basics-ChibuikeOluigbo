# Exercise 3 -> Correct
# Your solution comes here

time = int(input("Enter the number of seconds: "))


hours = (time // 3600) % 24
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60



clock = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
print(clock)