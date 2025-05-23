#  write a program to print following pattern 
'''
1 3 5 7 .... 100
steps
1. create variable number
2. number = 1
3. print number
4. number = number + 2
5. print number
6. number = number + 2
7. print number
'''
number = 1
while number <= 100:
    print (number, end = " ")
    number = number + 2
print()

'''
100 95 90 85 .... 0
steps
1. create variable number1
2. number1 = 100
3. print number1
4. number1 = number1 - 5
5. print number1
6. number1 = number1 - 5
7. print number1
'''
number1 = 100
while number1 >= 0:
    print(number1, end = " ")
    number1 = number1 - 5
print()

'''
1 4 9 16 .... 1000
steps
1. create variable number2
2. number2 = 1
3. print number2
4. number2 = number2 ** 2
5. print number2
6. number2 = number2 ** 2
7. print number2
'''
number2 = 1
n = 1
while number2 <= 1000:
    print(number2, end = " ")
    n = n + 1
    number2 = n ** 2
print()

'''
1 8 27 64 .... 1000
steps
1. create variable number3
2. number3 = 1
3. print number3
4. number3 = number3 ** 3
5. print number3
6. number3 = number3 ** 3
7. print number3
'''
number3 = 1
n = 1
while number3 <= 1000:
    print(number3, end = " ")
    n = n + 1
    number3 = n ** 3