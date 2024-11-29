upperLimit = int(input("Enter Upper Limit : "))
lowerLimit = int(input("Enter Lower Limit : "))

l = [] 

for i in range(lowerLimit, upperLimit + 1):
    if(i > 2):
        flag = True 
        for j in range(2, (i // 2) + 1):
            if(i % j == 0):
                flag = False 
                break 
        if(flag):
            l.append(i)
print('l ==<<<>>', l)