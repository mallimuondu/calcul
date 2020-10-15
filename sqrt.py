def sqr():
    number = int(input("enter a number to find the squre root: "))
    sqrt = number ** 0.5
    print("square root = :", sqrt)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        sqr()
    elif d == '' or d == ' ':
        print('you have inputed nothing try again')
        sqr()
sqr()