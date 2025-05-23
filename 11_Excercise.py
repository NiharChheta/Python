# Write a program to find out whether given name start with vowel or not.

name = input("Enter a name: ")

if name:
   
    if name[0] in "AEIOU":
        print("The name starts with a vowel.")
    else:
        print("The name does not start with a vowel.")


# Write a program to find out bigger triangle from given 2 triangles length and base.

base1 = float(input("Enter the base of triangle 1: "))
height1 = float(input("Enter the height of triangle 1: "))
base2 = float(input("Enter the base of triangle 2: "))
height2 = float(input("Enter the height of triangle 2: "))
area1 = 0.5 * base1 * height1
area2 = 0.5 * base2 * height2
if area1 > area2:
    print("Triangle 1 is bigger.")
elif area2 > area1:
    print("Triangle 2 is bigger.")
else:
    print("Both triangles are equal in area.")

# Write a program to find out whether business men has profit or loss from given purchase and sales price.

purchase_price = float(input("Enter the purchase price: "))
sales_price = float(input("Enter the sales price: "))
if sales_price > purchase_price:
    print("Profit")
if sales_price < purchase_price:
    print("Loss")

# Write a program to find out whether you should buy laptop from london or New york. Based on laptop price in given currency in Indian rupees.

# Fixed conversion rates (sample rates)
pound_to_inr = 113.67  # 1 British Pound = 113.67 Indian Rupees
dollar_to_inr = 85.52  # 1 US Dollar = 85.52 Indian Rupees


price_london = float(input("Enter the laptop price in London (in Pounds): "))
price_newyork = float(input("Enter the laptop price in New York (in Dollars): "))

# Convert the prices to Indian Rupees
price_london_inr = price_london * pound_to_inr
price_newyork_inr = price_newyork * dollar_to_inr

if price_london_inr < price_newyork_inr:
    print("Buy from London. The laptop is cheaper in INR!")
elif price_newyork_inr < price_london_inr:
    print("Buy from New York. The laptop is cheaper in INR!")
else:
    print("Both laptops cost the same in INR!")