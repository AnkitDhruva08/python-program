n = int(input('Enter value of N : '))

i = 0 
lenth = n* 10
l = []
while i <= n:
    if len(l) < n:
        for k in range(2, lenth):
            isPrime = True 
            for j in range(2, k // 2 + 1):
                if(k % j == 0):
                    isPrime = False
                    break 
            if isPrime and len(l) < n:
                l.append(k)
    else:
        i += 1
        break
                
print('l ===<<>>>', l)