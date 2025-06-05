def currency(inr):
    dollar = inr*0.012
    euro = inr*0.011
    pound = inr*0.0094
    yen = inr*1.7
    return dollar, euro, pound, yen
amount = float(input("Enter the amount in INR: "))
dollar, euro, pound, yen = currency(amount)
print(f"Amount in Dollar: {dollar}")
print(f"Amount in Euro: {euro}")
print(f"Amount in Pound: {pound}")
print(f"Amount in Yen: {yen}")
print()

# create keyword arguments function that 4 arguments. father name, mother name, brother name and sister name and display it with greet them with suitable prefix.

def greetFamily(wife, father, brother, mother):
    Wife = "Hello Mrs. " + wife
    Father = "Hello Mr. " + father
    Mother = "Hello Mrs. " + mother
    Brother = "Hello Mr. " + brother
    return Wife, Father, Mother, Brother

wife = input("Enter your wife's name: ")
father = input("Enter your father's name: ")
brother = input("Enter your brother's name: ")
mother = input("Enter your mother's name: ")

greetings = greetFamily(wife=wife, father=father, brother=brother, mother=mother)

for message in greetings:
    print(message)
