def libraryFine(arr, arr1):
    if arr[2] < arr1[2]:
        return 0
    if(arr[2] > arr1[2]):
        return (arr[2] - arr1[2]) * 10000
    dataValue = 0
    monthValues = 0
    if arr[0] > arr1 [0]:
        dataValue = arr[0] - arr1[0]
        
    if arr[1] > arr1[1]:
        monthValues = arr[1] - arr1[1]

    if(monthValues > 0):
        return monthValues * 500

    else:
        return dataValue * 15
        
# function call 
arr = list(map(int,input().split(' ')))
arr1 = list(map(int,input().split(' ')))
print(libraryFine(arr, arr1))
        