n = int(input('Enter Number Of Rows :'))

for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('')
    
# reverse of above program 
print('reverse of above program ')
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('')
    