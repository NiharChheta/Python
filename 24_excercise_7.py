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