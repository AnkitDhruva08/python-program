arr = list(map(int,input("Enter List Of Value : ").split(',')))

inversionCount = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j] and i < j):
            inversionCount += 1
print('inversionCount ===<<<>>>', inversionCount)