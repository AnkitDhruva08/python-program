Array = list(map(int, input("Enter List Of Values : ").split(',')))
Target = int(input("Enter Target Values : "))

flag = False
#  Two Pointer Approaches 
for i in range(len(Array)):
    for j in range(i + 1, len(Array)):
        if Target == Array[i] + Array[j]:
            flag = True
            break
if(flag):
    print("YES")
else:
    print("No")
        
   

