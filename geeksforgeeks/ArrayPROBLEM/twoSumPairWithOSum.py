arr = list(map(int, input("Enter List Of Values : ").split(',')))
l = [] 

arr.sort()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == 0:
            pair = [arr[i], arr[j]]
            if pair not in l:
                l.append(sorted([arr[i], arr[j]]))
                
print(l)
