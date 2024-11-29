n = int(input('Enter number ::'))
perfectNum = 0
l = []
for i in range(1, n//2 + 1):
    if(n % i == 0):
        perfectNum += i 
        l.append(i)
print('perfect number ==<<>>>', perfectNum)
print('l ===<<<>>>', l)
