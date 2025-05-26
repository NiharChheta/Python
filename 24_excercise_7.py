row = 1
while row <= 5:
    # Print spaces
    spaces = 5 - row
    while spaces > 0:
        print(" ", end=" ")
        spaces -= 1

    # Print stars
    column = 1
    while column <= row:
        print("*", end=" ")
        column += 1

    print()  # New line
    row += 1

print()

row = 1
while row <= 5:  # outer loop
    # print spaces
    space = 5 - row
    while space > 0:
        print(" ", end=' ')
        space = space - 1

    # print stars
    column = 1
    while column <= row:
        print("*", end='  ')  # extra space after * for triangle shape
        column = column + 1

    print()  # new line
    row = row + 1