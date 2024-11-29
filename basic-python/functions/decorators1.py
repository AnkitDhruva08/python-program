def logger(func):
    def sumOfValue(a, b):
        print(' I am inside Decorators :')
        addition = a + b 
        print('addition ===<<<>>>>', addition)
        result = func(a, b)
        print('result ==<<<>>>', result)
        return result
    return sumOfValue 

@logger
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a 


print(gcd(4,6))