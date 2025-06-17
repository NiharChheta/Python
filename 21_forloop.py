fruits = ["Mango", "Banana", "Guava", "Papaya", "Pomegranate", "Jackfruit", "Lychee", "Custard Apple", "Indian Gooseberry", "Sapota"]

print(fruits)

#display one fruit in one line 
#count items 
count=0
for item in fruits:
    print(item)
    count=count+1
print(count)

vegetables = ("Potato", "Tomato", "Onion", "Brinjal", "Okra", "Bitter Gourd", "Bottle Gourd", "Spinach", "Cabbage", "Cauliflower")
print("*"*100)
#print each and every vegetables in lower case 
for element in vegetables:
    print(element.lower())
    
print("*"*100)
#Dictionary
marks = {"Math": 88, "English": 75, "Science": 92, "History": 80, "Geography": 78, "Computer": 95}

#calculate total & Average
total = 0
count = 0
for subject in marks:
    print(subject + str(marks[subject]))
    total += marks[subject]
    count += 1

average = total / count
print(f"total = {total} average = {average}")

print()

# write a program to count vowels in given string 
# a e i o u 
name = input("Enter your name")
count = 0
print(name)
for letter in name:
    # print(letter)
    letter = letter.lower()
    if letter == 'a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count += 1
print(f"no of vowels = {count}")

print()

#print 1 to 10 using for loop 
for number in range(1,11):
    print(number)
    
    
#count odd number between 1 t0 10
count = 0
for number in range(1,11):
    if number%2==1:
        count+=1
print(f"odd number between 1 to 10 {count}")