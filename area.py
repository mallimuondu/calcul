print('''this are the things for area:
    a.circle
    b.squere
    c.rectangle
    d.triangle
    e.smicircle
    f.trapizium
    g.1/3 tiriangle
''')
a = input('you want to find the area of??:')
if a == 'a':
    b = int(input('input radius: '))
    c = 22/7*b*b
    print('the answer = ',c)
elif a == 'b' or a == 'c':
    d = int(input('insert length: '))
    e = int(input('insert widhth: '))
    f = d*e
    print('the area = ',f)
elif a == 'd':
    g = int(input('insert base: '))    
    h = int(input('insert hight: '))
    i = 0.5 * g * h
    print('the area = ',i)
elif a == 'e':
    j = int(input('insert radious: '))
    k = 22 * 0.5 * j * j / 7
    print('the area = ',k)
elif a == 'f':
    l = int(input('insert side a: '))    
    m = int(input('insert side b: '))
    n = int(input('insert hight: '))
    o = 0.5*a+b*h
    print('the area = ',o)
elif a == 'g':
    p = int(input('insert base: '))    
    q = int(input('insert hight: '))
    r = 0.025 * p * q
    print('the area = ',r)
    
    