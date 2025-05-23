# Write down a code for find the cube of a number

number = 1
cube = 1
number = int(input("Enter a number: "))
if number < 0: #< > <= >= == !=
    number = 0 - number
    print("The number is negative, converting to positive")
cube = number * number * number
print("The cube of the number is: ", cube)

height = 0
width = 0
height = int(input("Enter height: "))
width = int(input("Enter width: "))
if height == width:
    print("The shape is a square")
if height > width:
    print("The shape is a portait")
if height < width:
    print("The shape is a landscape")