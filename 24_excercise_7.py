row = 1
while row <= 5:  # outer loop
    spaces = 5 - row
    while spaces > 0:
        print(" ", end=" ")
        spaces -= 1

    column = 1
    while column <= row:
        print("*", end=" ")
        column += 1

    print()
    row += 1

print()

row = 1
while row <= 5:  # outer loop

    space = 5 - row
    while space > 0:
        print(" ", end=' ')
        space = space - 1

    column = 1
    while column <= row:
        print("*", end='  ')  # extra space after * for triangle shape
        column = column + 1

    print()
    row = row + 1

print()

row = 1
while row <= 5:
    # print leading spaces (two spaces per unit to balance with the numbers)
    space = 5 - row
    while space > 0:
        print("  ", end='')  # two spaces here
        space = space - 1

    # print alternating 1s and 0s with space between numbers
    column = 1
    num = row % 2
    while column <= row:
        print(num, end='   ')  # three spaces after each number for better pyramid shape
        num = 1 - num
        column = column + 1

    print()
    row = row + 1