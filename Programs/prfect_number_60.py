def isPerfect(number):
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    if sum_of_divisors == number:
        return True
    else:
        return False

# number = int(input("Enter a number: "))  # Example: 6 or 28
# result = isPerfect(number)
# print(result)