def reverseFunc(s1):
   reverseStr = ''
   for i in s1:
      reverseStr = i + reverseStr 
   return reverseStr 

s1 = str(input())

print(reverseFunc(s1))