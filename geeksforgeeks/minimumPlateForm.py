arr = list(map(int, input().split(',')))
dept = list(map(int,input().split(',')))

arr = sorted(arr)
dept= sorted(dept)
print('arrr', arr)
print('dept ', dept)
i = 0
j = 0
count = 0
maxPlateForm = 0

while i < len(arr)  and j < len(dept):
    if arr[i] < dept[j]:
            count +=1
            i += 1
            
    elif arr[i] > dept[j]:
            count -= 1
            j += 1
    maxPlateForm = max(maxPlateForm, count)
   
   
    

print('count ====<<<>>>>', count)
print('maxPlateForm ==<<<>>>', maxPlateForm)