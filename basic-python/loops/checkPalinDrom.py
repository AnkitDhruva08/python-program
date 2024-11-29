n = int(input('Enter A Number for check palindrom :'))

temp = n 
palinDromNum = 0

while temp != 0:
    palinDromNum = palinDromNum * 10 + temp % 10 
    print(palinDromNum)
    temp //= 10
    
print('palinDromNum ==<<>>', palinDromNum)
if(palinDromNum == n):
    print(' Yes is palinDromNum', palinDromNum)
    