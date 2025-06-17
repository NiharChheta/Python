# Create user defined function.
def getSquare(number):
    squre = number * number
    return squre

a = int(input("Enter a number: "))
b = int(input("Enter number: "))

aSqure = getSquare(a)
bSqure = getSquare(b)

cSquare = aSqure + bSqure
print(cSquare)