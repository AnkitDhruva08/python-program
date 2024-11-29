s = str(input())

s1 = list(s)
print('s1 ===<<<<>>>', s1)
mapDicTionary = {} 

for i in s1:
    if i in mapDicTionary:
        mapDicTionary[i] += 1
    else:
        mapDicTionary[i] = 1

for k, v in mapDicTionary.items():
    if v == 1:
        print('v ===<<<>>', k)
        break


    

