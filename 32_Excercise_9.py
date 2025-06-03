# Write a program to find the Octal number of Given Decimal number.
def getOctal(number):
    if number > 0:
        remainder = number % 8
        number = number // 8
        getOctal(number)
        print(remainder, end=' ')

number = int(input("Enter a decimal number: "))
getOctal(number)
print()
# Write a program to find the Factorial number of Given number.
def getFactorial(n, result=1):
    if n > 0:
        result *= n
        getFactorial(n - 1, result)
    else:
        print("Factorial:", result)

number = int(input("Enter the number: "))
getFactorial(number)
print ()

# Write a program to find hexadecimal number of Given Decimal number.

def getHexadecimal(number):
    hex_chars = "0123456789ABCDEF"
    if number > 0:
        remainder = number % 16
        number = number // 16
        getHexadecimal(number)
        print(hex_chars[remainder], end='')

number = int(input("Enter the number: "))
if number == 0:
    print("0")
else:
    getHexadecimal(number)