# Метод половинного деления

def F(x):
    return -18.85 + 10.89 * x - 4 * (x ** 2) + x ** 3

a = 0
b = 3
eps = 0.001

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('X = ', x)
print('F(X) = ', F(x))
