'''
decision making (if or if else)

4) write a program to accept month number from user and display name of the month

5) 

7) write a program to accept birth date and month from user. decide zodiac sign from below table 
Aries: March 21–April 19
Taurus: April 20–May 20
Gemini: May 21–June 21
Cancer: June 22–July 22
Leo: July 23–August 22
Virgo: August 23–September 22
Libra: September 23–October 22
Scorpio: October 24–November 21
Sagittarius: November 22–December 21
Capricorn: December 22–January 19
Aquarius: January 20–February 18
Pisces: February 19–March 20
'''

# Write dowm a code to accept month number from user and display name of the month.

month_number = 0
month_number = int(input("Enter the number of the month: "))
if month_number>=1 and month_number<=12:
    if month_number == 1:
        print("The month is January.")
    elif month_number == 2:
        print("The month is February.")
    elif month_number == 3:
        print("The month is March.")
    elif month_number == 4:
        print("The month is April.")
    elif month_number == 5:
        print("The month is May.")
    elif month_number == 6:
        print("The month is June.")
    elif month_number == 7:
        print("The month is July.")
    elif month_number == 8:
        print("The month is August.")
    elif month_number == 9:
        print("The month is September.")
    elif month_number == 10:
        print("The month is October.")
    elif month_number == 11:
        print("The month is November.")
    elif month_number == 12:
        print("The month is December.")
else:
    print("Invalid month number entered.")

# write a program to accept day of week and then display divas and ratri choghadiya.

'''
Step1) make a list of choghadiya for each days of the week.
Step2) accept day of week from user.
    Step3) if day == "Sunday":
        print("Sunday Day:", sunday_day, "Sunday Night:", sunday_night)
    else:
        print("Invalid day entered.")
'''

# Sunday Choghadiya
sunday_day = ["Udveg", "Chal", "Labh", "Amrut", "Kal", "Shubh", "Rog", "Udveg"]
sunday_night = ["Shubh", "Rog", "Udveg", "Chal", "Labh", "Kal", "Shubh", "Udveg"]

# Monday Choghadiya
monday_day = ["Amrut", "Kal", "Shubh", "Rog", "Udveg", "Labh", "Chal", "Amrut"]
monday_night = ["Chal", "Labh", "Amrut", "Kal", "Shubh", "Udveg", "Chal", "Amrut"]

# Tuesday Choghadiya
tuesday_day = ["Rog", "Udveg", "Chal", "Labh", "Amrut", "Kal", "Shubh", "Rog"]
tuesday_night = ["Kal", "Shubh", "Chal", "Udveg", "Amrut", "Rog", "Kal", "Chal"]

# Wednesday Choghadiya
wednesday_day = ["Labh", "Amrut", "Shubh", "Chal", "Rog", "Udveg", "Udveg", "Labh"]
wednesday_night = ["Udveg", "Chal", "Labh", "Shubh", "Kal", "Amrut", "Shubh", "Labh"]

# Thursday Choghadiya
thursday_day = ["Shubh", "Rog", "Kal", "Udveg", "Labh", "Amrut", "Amrut", "Shubh"]
thursday_night = ["Chal", "Udveg", "Kal", "Amrut", "Rog", "Labh", "Udveg", "Kal"]

# Friday Choghadiya
friday_day = ["Chal", "Labh", "Amrut", "Shubh", "Udveg", "Rog", "Kal", "Chal"]
friday_night = ["Labh", "Shubh", "Chal", "Rog", "Udveg", "Kal", "Labh", "Chal"]

# Saturday Choghadiya
saturday_day = ["Shubh", "Chal", "Rog", "Kal", "Amrut", "Udveg", "Chal", "Kal"]
saturday_night = ["Kal", "Amrut", "Shubh", "Labh", "Chal", "Rog", "Kal", "Shubh"]

day_name = input("Enter weekday name: ")

if day_name == "Sunday":
    print("Sunday Day:", sunday_day, "Sunday Night:", sunday_night)

elif day_name == "Monday":
    print("Monday Day:", monday_day, "Monday Night:", monday_night)

elif day_name == "Tuesday":
    print("Tuesday Day:", tuesday_day, "Tuesday Night:", tuesday_night)

elif day_name == "Wednesday":
    print("Wednesday Day:", wednesday_day, "Wednesday Night:", wednesday_night)

elif day_name == "Thursday":
    print("Thursday Day:", thursday_day, "Thursday Night:", thursday_night)

elif day_name == "Friday":
    print("Friday Day:", friday_day, "Friday Night:", friday_night)

elif day_name == "Saturday":
    print("Saturday Day:", saturday_day, "Saturday Night:", saturday_night)
else:
    print("Invalid day entered.")


# write a program to accept birth date and month from user to decide zodiac sign.

'''
Step1) accept day and month from user.
Step2) if month == "march" and day >= 21 or month == "april" and day <= 19:
        print("Your zodiac sign is Aries.")
Step3) else:

'''

day = int(input("Enter your birth day: "))
month = input("Enter your birth month: ")
if day>=1 and day<=31:
    if (month == "march" and day >= 21) or (month == "april" and day <= 19):
        print("Your zodiac sign is Aries.")
    elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
        print("Your zodiac sign is Taurus.")
    elif (month == "may" and day >= 21) or (month == "june" and day <= 21):
        print("Your zodiac sign is Gemini.")
    elif (month == "june" and day >= 22) or (month == "july" and day <= 22):
        print("Your zodiac sign is Cancer.")
    elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
        print("Your zodiac sign is Leo.")
    elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
        print("Your zodiac sign is Virgo.")
    elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
        print("Your zodiac sign is Libra.")
    elif (month == "october" and day >= 24) or (month == "november" and day <= 21):
        print("Your zodiac sign is Scorpio.")
    elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
        print("Your zodiac sign is Sagittarius.")
    elif (month == "december" and day >= 22) or (month == "january" and day <= 19):
        print("Your zodiac sign is Capricorn.")
    elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
        print("Your zodiac sign is Aquarius.")
    elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
        print("Your zodiac sign is Pisces.")
else:
    print("Invalid date or month entered.")