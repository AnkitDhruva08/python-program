arr = list(map(int, input('Enter List Of Values : ').split(',')))
subArry = []

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(len(arr[i:j]) != 0):
            subArry.append(arr[i:j])
print('subArray ===<<>>>', subArry)