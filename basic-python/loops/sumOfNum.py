n = int(input('enter number :::'))

sum1 = 0

temp = n 
while temp != 0:
    sum1 +=  temp % 10 
    temp = temp //10
print('sum1 ==<<<>>', sum1)