def addition():
    number1 = int(input('insert first number: '))
    if number1 == '' or number1 = ' ':
        print('you have inputed nothing')
    number2 = int(input('insert first number: '))
    if number2 == '' or number2 = ' ':
        print('you have inputed nothing')
    c = number1+number2
    print('the answer is = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        addition()
    elif d == '' or d = ' ':
        print('you have inputed nothing')
addition()
