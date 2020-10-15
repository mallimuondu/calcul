def addition():
    number1 = int(input('insert first number: '))
    number2 = int(input('insert first number: '))
    c = number1+number2
    print('the answer is = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        addition()
addition()
