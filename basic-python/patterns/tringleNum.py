n = int(input("Enter A Number :"))

for i in range(1, n+1):
    #for nested loop 
    for j in range(i):
        print(i,end='')
    print(' ')