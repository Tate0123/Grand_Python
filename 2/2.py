import math
t = float(input('Введите t'))
a = t + 1
b = 4*t
c = 3*t
if a == 0:
    x = -c/2*a
else:
    D = b**2 - 4*a*c
    print('D:', D)
    print('a:', a)
    print('b:', b)
    print('c:', c)
    if D >= 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print('x1 =', x1, 'x2 =', x2)
    else:
        print('D < 0')