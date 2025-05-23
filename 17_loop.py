# Write a program to find out the factorial of given number.
'''
Steps
1. create a variable and factorial.
2. Take input from the user.
3. store 1 in factorial.
4. Create a while loop to calculate the factorial.
5. Print the final result.
'''

number = 0 
factorial = 1
number = int(input("Enter a number: "))
while number > 0:
    factorial = factorial * number
    number = number - 1
print("The factorial is: ", factorial)