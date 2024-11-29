def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
n = int(input("Please enter a number to generate the Fibonacci series: "))
print("The Fibonacci series is:")
for i in range(0, n):
    print(fibonacci(i))