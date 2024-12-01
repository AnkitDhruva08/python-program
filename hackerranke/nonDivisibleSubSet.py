from itertools import permutations
arr = list(map(int,input('Enter A list of Values : ').split(',')))
k = int(input('Enter Value of K : '))

perm = list(permutations(arr, k))

for p in perm :
    if(sum(p) % k != 0):
        print(p)

