class Cricketer:
    # constructor function
    def __init__(self, name, match, runs, balls, fifties, centuries):
        print("constructor function called...")
        self.name = name
        self.match = match
        self.runs = runs
        self.balls = balls
        self.fifties = fifties
        self.centuries = centuries

        if self.match != 0:
            self.average = self.runs / self.match
        else:
            self.average = 0

        if self.match != 0:
            self.fifty_rate = (self.fifties / self.match) * 100
        else:
            self.fifty_rate = 0

        if self.match != 0:
            self.century_rate = (self.centuries / self.match) * 100
        else:
            self.century_rate = 0

    def display(self):
        print("Player Stats")
        print("Name:", self.name)
        print("Matches:", self.match)
        print("Runs:", self.runs)
        print("Balls Faced:", self.balls)
        print("Average:", round(self.average, 2))
        print("Fifties:", self.fifties)
        print("Centuries:", self.centuries)
        print("Fifty Rate (%):", round(self.fifty_rate, 2))
        print("Century Rate (%):", round(self.century_rate, 2))

def get_int_input(number):
    while True:
        try:
            value = int(input(number))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_name_input(alphabet):
    while True:
        name = input(alphabet)
        if name.isalpha():
            return name
        else:
            print("Invalid name! Please enter only alphabets.")

print("Enter details for Player 1")
name = get_name_input("Enter player name: ")
match = get_int_input("Enter number of matches played: ")
runs = get_int_input("Enter total runs: ")
balls = get_int_input("Enter total balls faced: ")
fifties = get_int_input("Enter number of fifties: ")
centuries = get_int_input("Enter number of centuries: ")

p1 = Cricketer(name, match, runs, balls, fifties, centuries)
p1.display()

print("Enter details for Player 2")
name = get_name_input("Enter player name: ")
match = get_int_input("Enter number of matches played: ")
runs = get_int_input("Enter total runs: ")
balls = get_int_input("Enter total balls faced: ")
fifties = get_int_input("Enter number of fifties: ")
centuries = get_int_input("Enter number of centuries: ")

p2 = Cricketer(name, match, runs, balls, fifties, centuries)
p2.display()
