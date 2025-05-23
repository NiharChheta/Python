# Question 1

user1 = input("Enter the number: ")
user2 = input("Enter the number: ")
user3 = input("Enter the number: ")
user4 = input("Enter the number: ")
user5 = input("Enter the number: ")
numbers = [user1, user2, user3, user4, user5]
print(numbers)
minimum = min(numbers)
print(minimum)
maximum = max(numbers)
print(maximum)
numbers.sort()
print(numbers)


# Question 2 tuple program
fruits = ("apple", "banana", "mango", "orange")
print(fruits)
print(fruits[2])
position = fruits.index("orange")
print("Position of orange is:", position)

fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
fruits.append("kiwi")
print(fruits)

# Question 3 Dictionary program

marks = {"Math": 85, "Science": 90, "English": 78}

marks["Computer"] = 92
print(marks)

highest_mark = max(marks)
print("Subject with highest marks:", highest_mark)

# Question 4

student1 = input("Enter the name of student 1: ")
student2 = input("Enter the name of student 2: ")
student3 = input("Enter the name of student 3: ")
students = [student1, student2, student3]

print("The list of students is:")
print(students)

subjects = ("Math", "Science", "English")
print(subjects)

marks = [[85, 90, 78], [88, 92, 80], [90, 85, 95]]
print(marks)

dictionary = {
    student1: {subjects: [85, 90, 78]},
    student2: {subjects: [88, 92, 80]},
    student3: {subjects: [90, 85, 95]}
}
print(dictionary)

# Question 5

total_minutes = input("Enter total minutes: ")
total_minutes = int(total_minutes)

hours = total_minutes // 60

minutes = total_minutes % 60
print(hours, "hours", minutes, "minutes.")
