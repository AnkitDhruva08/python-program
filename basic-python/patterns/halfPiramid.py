n = int(input('Enter Number of Rows :'))

for i in range( n):
    for j in range( n + 1 - i):
        print(j, end='')
    print('')
        