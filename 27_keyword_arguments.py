# write a program to implement Pythagoras Theorem:

#create user defined function 

#with return value with argument(input)
def getSquare(number):
    #create local variable
    square = number * number
    return square
# Without return value without argument
def printLine():
    print("*" * 125)
    return None 

printLine() #calling function printline
a = int(input("Enter value for A"))
a_square = getSquare(a) #calling function
b = int(input("Enter value for B"))
b_square = getSquare(b) #calling function

c_square = a_square + b_square
printLine()
print(c_square)
printLine()

# With return value Without argument
from datetime import datetime 
from playsound3 import playsound

def getDateTime():
    now = datetime.now()
    return now 

def getDate():
    now = datetime.now()
    # 29-05-2025 
    today = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
    return today

def getTime():
    now = datetime.now()
    # 17:56 
    time = str(now.hour) + ":" + str(now.minute)
    return time 

def ringBell():
    playsound("bell.mp3")
    
#without return value With argument 
#call function 
result = getDateTime()
print(result)

print(getDate())
print(getTime())
ringBell()

#default argument function 
def getSquare(x,y=2):
    # print(x)
    # print(y)
    result = (x * x) + (2 * x * y) + (y * y) 
    return result

result = getSquare(10,5)
print(result)
result = getSquare(5)
print(result)

def getMeritTotal(maths,science,english,hindi,gujarati,computer):
    total = maths + science + english
    return total 


maths = 80
science = 90 
english = 95 
hindi = 41
gujarati = 51
computer = 35 
 
total = getMeritTotal(maths,science,hindi,gujarati,computer,english)
print(total)