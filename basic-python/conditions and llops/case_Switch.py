choic = int(input("enter your choice :::"))
match(choic):
    case 1:
        a = int(input('enter value of a:::'))
        b = int(input('enter value of b:::'))
        
        print("Sum of the a And b ===<<<<>>>>", a+b)
        
    case _ :
        print('your choice is invalid')