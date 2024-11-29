n = int(input())
n1 = str(n)
armStrong = 0
for i in n1:
    num = int(i)**3
    armStrong += num 
print('armStrong ===<<>>>', armStrong)
if(armStrong == n):
    print('yes it is armstrong number')
    