lowerLimit = int(input()) 
uperLimit = int(input()) 

for i in range(lowerLimit, uperLimit):
    is_prime = True
    for j in range(2, (i//2) +1):
        if(i%j == 0):
            is_prime = False
            break
    if is_prime:
        print('prime number is ===<<<>>>', i)