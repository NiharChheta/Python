# Write a code for 24 hours format to 12 hours format

hours = 0
minutes = 0
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
if hours > 12:
    hours = hours - 12
    print("The time is: ", hours, ":", minutes, "PM")
else:
    print("The time is: ", hours, ":", minutes, "AM")

# write a code if person is eligible for applying for civil service exam.

age = 0
age = int(input("Enter age: "))
if 18 <= age <= 36:
    print("You are eligible for applying for civil service exam")
else:
    print("You are not eligible for applying for civil service exam")