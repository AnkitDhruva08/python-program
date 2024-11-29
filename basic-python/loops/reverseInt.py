n = int(input('Enter A Number :'))

Num = n 
reversedNum = 0

while n != 0:
    reversedNum = reversedNum * 10 + n % 10 
    n = n//10 
print(reversedNum)
    
    