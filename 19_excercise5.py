# Write a program to find out only compound interest from the given amount, rate and year.
'''
Steps
1. Get the amount, rate of interest, and time period from the user.
2. CI = amount * ROI / 100
3. time period = time period - 1
4. amount = amount + CI
5. CI = amount * ROI / 100
6. time period = time period - 1
7. amount = amount + CI
8. CI = amount * ROI / 100
9. time period = time period - 1
10. amount = amount + CI
11. print CI
'''

amount = 0
ROI = 0
time_period = 0
amount = int(input("Enter amount: "))
ROI = int(input("Enter rate of interest: "))
time_period = int(input("Enter time period: "))
CI = 0

while time_period > 0:
    CI = amount * ROI / 100
    time_period = time_period - 1
    amount = amount + CI
print(CI)

# write a program to find out power of given base and exponent.

'''
Steps
1. Get the base and exponent from the user.
2. power = 1
3. exponent = exponent - 1
4. power = power * base
5. exponent = exponent - 1
6. power = power * base
7. exponent = exponent - 1
8. power = power * base
9. print(power)
'''

base = 0
exponent = 0
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
power = 1
while exponent > 0:
    power = power * base
    exponent = exponent - 1
print(power)

# write a program to make sum of all digit in given number.

'''
Steps
1. Get the number from the user.
2. sum = 0
3. number = number // 10
4. sum = sum + number % 10
5. number = number // 10
6. sum = sum + number % 10
7. number = number // 10
8. sum = sum + number % 10
9. print(sum)
'''
number = 0
number = int(input("Enter number: "))
sum = 0
while number > 0:
    sum = sum + number % 10
    number = number // 10
print(sum)