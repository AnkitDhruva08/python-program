n = int(input("enter Number : "))
first = 0
second = 1
l = [first, second]

for i in range(n):
    if i <= 1:
        result = i 
        
    else:
        result = first + second 
        first = second 
        second = result 
        l.append(result)
print(l)