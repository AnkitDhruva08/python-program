num1 = int(input('Enter First Number ::'))
num2 = int(input('Enter Second Number ::'))

if num1 < num1: 
    value = num1 
else:
    value = num2 
    
for i in range(1, value + 1):
    if(num1 % i == 0 and num2 % i == 0):
        print('i ==<<<>>', i)