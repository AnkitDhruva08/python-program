arr = list(map(int,input('enter value of array :').split(',')))
currunt = 0
prev = -1
step = 0 

while currunt < len(arr):
    maxValus = max([prev + ix + ve for ix, ve in enumerate(arr[prev + 1 : currunt +1])])
    print('maxValus ====<<<>>>', maxValus)
    if maxValus > currunt :
        currunt = maxValus
        prev = currunt
        step = step +1
        
print('step ===<<<>>>', maxValus)