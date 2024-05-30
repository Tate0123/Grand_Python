# Метод Ньютона

def F(x):
    return -18.85 + 10.89 * x - 4 * (x ** 2) + x ** 3

def F1(x):
    return x**3 - 3.9*x**2 + 10.24*x - 16.85

a = 0
b = 3
eps = 0.001

x1 = (a + b) / 2
x0 = x1 + 2*eps

while abs(x1 - x0) > eps:
    x0 = x1
    x1 = x0 - F(x0) / F1(x0)

print('X = ', x1)
print('F(X) = ', F(x1))
