def permutationApproach(arr, start = 0):
    if start == len(arr) - 1:
        print(arr)
        return 
    
    for i in range(start, len(arr)):
        # Swap elements to generate a new permutation
        arr[start], arr[i] = arr[i], arr[start]
        permutationApproach(arr, start + 1)
        
        # Swap back to backtrack
        arr[start], arr[i] = arr[i], arr[start] 
        
#  function call 
arr = list(map(int,input('Enter List Of values : ').split(',')))
print(permutationApproach((arr)))