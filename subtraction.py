def subtraction():
    number1 = int(input('insert first number: '))
    if number1 == '' or number1 == ' ':
        print('you have inputed the wrong thing')
    number2 = int(input('insert first number: '))
    if number2 == '' or number2 == ' ':
        print('you have inputed the wrong thing')
    c = number1-number2
    print('the answer is = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        subtraction()
    elif d == '' or d == ' ':
        print('you have inputed the wrong thing')
subtraction()
