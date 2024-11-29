s1 = str(input())
s2 = str(input())
print('s1 ===<<<>>>', s1)
print('s2 ===<<<>>>', s2)
leftRotate = s1[2:] + s2 [:2]
print('leftRotate ===<<<>>>', leftRotate)
rightRotate = s1[-2:] + s2[:-2]
    
print('rightRotate ===<<<>>>', rightRotate)

    