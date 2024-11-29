n = int(input('Enter A Number: '))

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
for j in range(n - 2, -1, -1):
    print(" " * (n - j - 1) + "*" * (2 * j + 1))
    