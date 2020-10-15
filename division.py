def division():
    try:
        number1 = int(input('insert first number: '))
        string_number1 = str(number1)
        if number1 == '' and number1 = ' ':
            print('you have inputed nothing try again')
    except ValueError:
        print ('That is not a number try again')
        division()
    try:
        number2 = int(input('insert first number: '))
        string_number2 = str(number2)
        if number2 == '':
            print('you have inputed nothing try again')
    except ValueError:
        print ('That is not a number try again')
        division()
    c = number1/number2
    print('the answer is = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        division()
division()
