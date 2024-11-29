# Read input for the array and limits
nums = list(map(int, input("Enter numbers separated by commas: ").split(',')))
lower = int(input('Enter Lower Limit: '))
upper = int(input('Enter Upper Limit: '))
countValue = 0

# Sort the array
nums.sort()

# Iterate over each element in the array
for i in range(len(nums) - 1):
    left = i + 1
    right = len(nums) - 1
    
    # Move `left` pointer to find the minimum sum >= lower
    while left <= right and nums[i] + nums[left] < lower:
        left += 1
    
    # Move `right` pointer to find the maximum sum <= upper
    while left <= right and nums[i] + nums[right] > upper:
        right -= 1
    
    # Count all valid pairs for the current `i`
    if left <= right:
        countValue += (right - left + 1)

# Output the result
print('CountValue ==<<>>', countValue)
