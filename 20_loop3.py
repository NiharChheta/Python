'''
    write a program to find out reverse of given no 
    input : 1234 
    output : 4321
    steps 
    -----------------------
    1   create variable number,reminder,reverse = 0 
    2   accept input from user into number (assume 1234)
    
    3   reminder(4) = number % 10 
    4   reverse(4) = (reverse * 10 )+ reminder
    5   number(123) = number // 10
    
    6   reminder(3) = number % 10 
    7   reverse(43) = (reverse * 10)+ reminder   
    8    number(12) = number // 10
    
    9   reminder(2) = number % 10 
    10   reverse(432) = (reverse * 10)+ reminder
    11    number(1) = number // 10
    
    12   reminder(1) = number % 10 
    13   reverse(4321) = (reverse * 10) + reminder
    
'''
number = reminder = reverse = 0 
number = int(input("Enter number"))

while number>0:
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number // 10

print(f"reverse = {reverse}")