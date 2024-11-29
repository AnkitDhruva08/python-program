def dictFun(mydic):
    # Sort dictionary keys and return as a list
    l = sorted(mydic)
    return l[:2] 

# Read comma-separated input and split into list
l1 = list(map(str, input().split(',')))

# Initialize an empty dictionary
myDict = {}
for i in l1:
    # Check if the key already exists in myDict
    if i in myDict:
        myDict[i] += 1  # Increment count if key exists
    else:
        myDict[i] = 1   # Initialize count to 1 if key doesn't exist

# Print the dictionary and sorted keys
print('myDict ===<<<<>>>', myDict)
print(dictFun(myDict))
