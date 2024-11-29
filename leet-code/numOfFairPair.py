nums = list(map(int,input().split(',')))

lower = int(input('Enter Lower Limit :'))
upper = int(input("Enter Uper Limit :"))
countValue = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if(nums[i] + nums [j] >= lower and nums[i] + nums [j] <= upper):
            print('Sum of i, j ==>>>', nums[i] + nums [j])
            countValue +=1 
print('countValues ===<<<>>>', countValue)