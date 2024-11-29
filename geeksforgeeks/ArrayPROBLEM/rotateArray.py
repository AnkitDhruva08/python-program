arr = list(map(int, input('Enter List Of Values : ').split(',')))
d = int(input("Enter Number of Rotation : "))

arr1 = arr[d:len(arr)] + arr[ : d]
arr2 = arr[ : d]
print('arr1 ===<<>>>', arr1)
print(arr2)