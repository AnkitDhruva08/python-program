from itertools import permutations
arr = list(map(int,input('Enter List Of Values : ').split(',')))
perm = list(permutations(arr))

for p in perm:
    print(p)