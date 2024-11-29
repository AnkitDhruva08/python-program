rows = int(input("Enter Number Of  Rows : "))

for i in range(rows):
    print(' ' * (rows - i - 1) + "*" * (2 * i + 1))

for j in range(rows - 1 , - 1, -1):
    print(' ' * (rows - j - 1) + "*" * (2 * j + 1))
    