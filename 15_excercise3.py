#  write a program to check whether given year is leap year or not.

'''
Step 1) input year from the user.
Step 2) year should >= 1582.
step 3) divide the year by 4
Step 4) if the result is an integer number then divide the year by 100.
Step 5) if result is in a decimal number then the year is leap year.
step 6) if result is in an integer number then divide the year by 400.
Step 7) if result is in an integer number then the year is leap year.
Step 8) else: the year is not leap year.
Step 9) else: Enter a valid year.
'''

year = 0
year = int(input("Enter year: "))
if year >= 1582:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("The year is a leap year.")
        else:
            print("The year is not a leap year.")
    else:
        print("The year is not a leap year.")
else:
    print("Enter a valid year.")