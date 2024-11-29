first = 0 
second = 1 
l = []
for i in range(0, 7):
    if i <= 1:
        result = i
    else :
        result = first + second
        first = second
        second = result
    print(result)
        
    l.append(result)
      
print('l ===<<<>>>', l)