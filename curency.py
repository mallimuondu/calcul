def dollers_ksh():
    a = int(input('insert dollers$ to ksh$:'))

    b = 108.59
    c = a*b
    print('your ammount  = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        dollers_ksh()
dollers_ksh()

def ksh_dollers():
    a = int(input('insert ksh$ to dollers$:'))

    b = 0.0092
    c = a*b
    print('your ammount  = ',c)
    d = input('do you want to try again (y/n): ')
    if d == 'y':
        ksh_dollers()
ksh_dollers()