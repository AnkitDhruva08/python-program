n = int(input('Enter Number to check Prime or not :'))

flag = True
for i in range(2, (n // 2) + 1):
    
    if(n % i == 0):
        flag = False
        break 

if(flag):
    
    print(' n is prime number :')
else:
    print('Not A prime Number')
    