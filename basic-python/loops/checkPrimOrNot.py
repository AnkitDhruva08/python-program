nums = [x for x in range(10, 100) ]
l = []
for i in nums:
    if i > 2:
        isPrime = True
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                isPrime = False
                break 
        if isPrime:
            l.append(i)
print('nums ===<<<>>>', l)