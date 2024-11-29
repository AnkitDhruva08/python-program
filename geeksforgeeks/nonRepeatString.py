s = str(input())

char_space=[0]*26
print('char_space ===<<<>>>', char_space)
for i in s:
    print('char_space first loop ===<<<>>>', char_space)
    char_space[ord(i)-97]+=1
for i in s:
    print('char_space  second loop===<<<>>>', char_space)
    if char_space[ord(i)-97]==1:
        print('i ==<<>>>', i)
       
    