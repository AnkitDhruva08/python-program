num1 = int(input('Enter First Number ::'))
num2 = int(input('Enter Second Number ::'))

if num1 > num2:
    Value = num1
else:
    Value = num2 
    
while(True):
    if(Value % num1 == 0 and Value % num2 == 0):
        break 
    Value += 1
print('value ===<<<>>>', Value)