n = int(input('Enter a Number :'))

l = []

for i in range(2, n//2+1):
    if(n % i == 0):
        print('i ===<<<>>>', i)
        flag = True
        for j in range (2, i //2 + 1):
            if i % j == 0 :
                print('<<<<<<<<<<<<<<', i)
                flag = False 
                break
        if flag:
            l.append(i)
print('l ', l)
            
    