arr = list(map(int,input().split(',')))

myDict = {}

for i in arr:
    if i in myDict:
        myDict[i] +=1
    else:
            
        myDict[i] = 1
        
print('mydict ==<<<>>>', myDict)

maxKey = max(myDict, key = myDict.get)
print(maxKey)
maxValue = myDict[maxKey]
print('max key ', maxValue)
allKey = sorted(myDict.keys())
minKey = allKey[0]
maxRange = allKey[-1]
missingKey = []
missingKey.append(maxKey)
for i in range(minKey, maxRange +1):
    if i not in allKey:
        missingKey.append(i)
        break 
    
print('missing array ', missingKey)
