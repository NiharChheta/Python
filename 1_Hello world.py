'''
Introduction
'''
print('Name : Nihar Chheta')
print("Qualification : Currently pursuing M. SC. in Elecretical Engineering")
print("Mobile : +45 91725558")
print('''Address : Skejby VÆnge 18 1A, 
      8200 Aarhus N, 
      Denmark''')

#variables and input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is:", name)
print("Your age is:", age)

# string
line = "Hello how are you?"
print(line)
print(line[0:5])
print(line[6:9])
print(line[10:])
print(line*2)

#List
Favorite_Dishes = ['Gujarati', 'Italian', 'Punjabi', 'Chinese', 'South Indian']
Friend_Details = ['Hiren', '29', 'Male', 'Engineer', 'New Zealand']
print(Favorite_Dishes)
print(Friend_Details)
print(Favorite_Dishes[0:2])
print(Friend_Details[0:2])
print(Favorite_Dishes[1:3] + Friend_Details[0:1])
Friend_Details[0] = "Hiren Sakariya"
print(Friend_Details)
Friend_Details[0] = "Kapil Korat"
Friend_Details[3] = "Employe"
Friend_Details[4] = "India"
print(Friend_Details)
print(Friend_Details[0:1] + Favorite_Dishes[2:5])

#List related methods
Fruits = []
print(Fruits)

# If you want to insert a value end od the list
Fruits.append("Apple")
Fruits.append("Banana")
Fruits.append("Mango")
Fruits.append("Orange")
print(Fruits)
 
# If you want to insert a value at the beginning of the list
Fruits.insert(0, "Grapes")
print(Fruits)

# If you want to remove a value from the list
Fruits.remove("Mango")
print(Fruits)

# If you want to remove a first value.
Fruits.pop(0)
print(Fruits)

#If you want ot add two lists
vegis = ["Potato", "Tomato", "Onion"]
Fruits.extend(vegis)
print(Fruits)

#removing the values
vegis.clear()

position = Fruits.index('Apple')
print(position)

Fruits.append('kiwi')
print(Fruits)
#count of of kiwi 
total = Fruits.count('kiwi')
print(total)