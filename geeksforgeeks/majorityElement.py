arr = list(map(int, input().split(',')))

majritycout = {}


for i in arr:
    if i in majritycout:
        majritycout[i] += 1
    else:
        majritycout[i]  = 1
maxCount = max(majritycout, key = majritycout.get)
maxValue = majritycout[maxCount]
if(maxValue > 1):
    print(maxValue)      
else :
    print(maxValue) 