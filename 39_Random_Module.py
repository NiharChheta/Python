import random as rd 
#here rd as alias for random 

#generate random number between 0.0 and 1.0 
print(rd.random())

#generate float random number between 10 to 99
print(rd.uniform(10,99))

#generate integer random number between 10 to 99
print(rd.randint(10,99))

#generate integer random number between 10 to 100 divisible by 10
print(rd.randrange(10,99,10))

print()

# example of choice & choices 
import random as rd 

# create list 
ipl_teams_2025 = ["Chennai Super Kings", "Kolkata Knight Riders", "Rajasthan Royals", "Royal Challengers Bengaluru", "Punjab Kings", "Mumbai Indians", "Sunrisers Hyderabad", "Delhi Capitals", "Gujarat Titans", "Lucknow Super Giants"]

print("next winner in ipl will be ",rd.choice(ipl_teams_2025))


print("in ipl 2026 4 qualifiers will be ",rd.choices(ipl_teams_2025,k=4))

rd.shuffle(ipl_teams_2025)
print("point table in 2026 will be below")
print(ipl_teams_2025)