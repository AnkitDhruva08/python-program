s = input("Enter A String : ")

l = list(s)
print(l)
subStringList = []

for i in range(len(l)):
    for j in range(i, len(l)):
        if(len(l[i:j]) > 0):
            subStringList.append(l[i:j])
        
print('subStringList ===<<<>>>', subStringList)