arr = list(map(str,input().split(',')))
arr.sort()
prefix=''
check=arr[0]
print('check ==<<>>>', check)
for i in range(len(check)):
    c=0
    for j in arr:
        if check[i]==j[i]:
            print('i am inside if')
            c+=1
        else:
            break
    print('c ==<<<>>', c)
    if c==len(arr):
        prefix+=check[i]
    else:
        break
       
print('prefix ==<<>>>>', prefix)