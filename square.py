def squre():
    a = int(input('insert a number to find its squre: '))
    b = a*a
    print('the squre is = ',b)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        squre()
squre()