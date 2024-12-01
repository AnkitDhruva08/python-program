n = int(input("Enter Values Of : "))
spaceStation = list(map(int,input("Enter List of Values : ").split(' ')))

spaceStation.sort()
distance = spaceStation[0]

for i in range(1, len(spaceStation)):
    distance = max(distance, ((spaceStation[i] - spaceStation[i - 1])//2))
    
maxDistance = max(distance, n - 1 - spaceStation[-1])

print('maxDistance ====<<<>>>>', maxDistance)
 

    
