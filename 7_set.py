set = {50, 60, 70, 80, 90}
print(set)
set.add(100)
print(set)
set.remove(50)
print(set)

#Arithmatic operations
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2
reminder = num1 % num2
power = num1 ** num2
floor_div = num1 // num2
print("Reminder: ", reminder) # print("Reminder: " + str(reminder))
print("Power: ", power)
print("Floor Division: ", floor_div)
print("Sum: ", sum)
print("Difference: ", diff)
print("Product: ", prod)
print("Division: ", div)