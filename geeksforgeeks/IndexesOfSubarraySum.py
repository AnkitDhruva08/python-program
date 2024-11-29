print('hello python')

# Input and initialization
arr = list(map(int, input('Enter values of n separated by commas: ').split(',')))
print('arr ===<<<>>>>', arr)
n = int(input('Enter value of n: '))
s = int(input('Enter value of s: '))
currentSum = 0
startIndex = 0
endIndex = 0
result = []

while endIndex < n:
    currentSum += arr[endIndex]  
    
    # Shrink the window from the left if currentSum exceeds s
    while currentSum > s and startIndex < endIndex:
        currentSum -= arr[startIndex]
        startIndex += 1
        
    if currentSum == s:
        result = [startIndex + 1, endIndex + 1]  
        print('result ===<<<>>>', result)
        break 
    
    endIndex += 1  

# If no subarray was found, print -1
if not result:
    result = [-1]

print('result ===<<<>>>', result)
