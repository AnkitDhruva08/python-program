n = int(input('Enter Number :'))

for i in range(2, n+1):
    if (n % (i * i) == 0):
        print(i)