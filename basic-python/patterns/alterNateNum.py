n = int(input('Enter Number of Rows :'))

i = 1 

while i <= n:
    j = 1 
    while j <= i:
        print(i * 2 - 1 , end='')
        j += 1 
    i += 1
    print('')