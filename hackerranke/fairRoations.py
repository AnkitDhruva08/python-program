def fairRotation(arr):
    odd = [i for  i in range(len(arr)) if arr[i] % 2 == 1]
    breads = 0
    
    if(len(odd) % 2 == 1):
        return 'No'
    
    for i in range(0, len(odd)-1, 2):
        breads = breads + odd[i + 1] - odd[i]
        
    return 2 * breads





# function call 
n = int(input('Enter Values of N : '))
arr = list(map(int,input('Enter List Of Values : ').split(',')))
print(fairRotation( arr))

