import math
def getToatlX(a,  arr):
    lcmOfA = math.lcm(*a)
    counter = 0
    i = 1
    while i * lcmOfA <= min(arr):
        divFlag = True 
        
        for j in arr:
            if(j % (i * lcmOfA ) != 0):
                divFlag = False 
        if(divFlag):
            counter += 1
        i += 1
    return counter 

a = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

print(getToatlX(a, arr))

                