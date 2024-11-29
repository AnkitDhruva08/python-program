arr = list(map(int, input("Enter Number Of List : ").split(',')))
k = int(input("Enter K Value : "))

prefixSum = {}
maxLength = 0
currentSum = 0

for i in range(len(arr)):
    currentSum += arr[i]
    print('currentSum ==<<<>>>', currentSum)
    if(currentSum == k):
        maxLength += 1 
    print('maxLength ===<<<>>>', maxLength)
    if((currentSum - k) in prefixSum):
        maxLength = max(maxLength, i - prefixSum[currentSum - k])
    if(currentSum not in prefixSum):
        prefixSum[currentSum] = i 
print('maxLength result <<>>>', maxLength)
print('prefixSum result <<>>>', prefixSum)
        
