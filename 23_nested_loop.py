fruits = ["Mango", "Banana", "Guava", "Papaya", "Pomegranate", "Jackfruit", "Lychee", "Custard Apple", "Indian Gooseberry", "Sapota"]
print(fruits)

#print list in reverse 
for item in reversed(fruits):
    print(item)
    
#print 10 to 1 
for number in range(10,0,-1):
    print(number,end=' ')
print()

'''
write a program to print following pattern (only one astrik at time will be displayed)

*
* *
* * *
* * * *
* * * * *
'''
row = 1
while row<=5: #outer loop
    column=1
    while column<=row: #inner loop 
        print('*',end=' ')
        column=column+1
    print(" ") #new line 
    row=row+1

print()

'''
write a program to print following pattern (only one astrik at time will be displayed)
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
row=5
while row>=1:
    column=1
    while column<=row:
        print(f'{column} ',end=' ')
        column=column+1
    print('') #new line
    row=row-1
