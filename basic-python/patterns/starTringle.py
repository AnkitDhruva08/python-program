rows = int(input("Enter A Number for Print Tringle :"))

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

