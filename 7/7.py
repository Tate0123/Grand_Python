import numpy as np

A=np.genfromtxt('Text\А.txt')

print('Исходный массив A')
print(A)

B=np.genfromtxt('Text\В.txt')
print('Исходный массив B')
print(B)

Q=np.genfromtxt('Text\Q.txt')
print('Исходный массив Q')
print(Q)

R=np.genfromtxt('Text\R.txt')
print('Исходный массив R')
print(R)

x = np.dot(B,Q)
print ('x =', x)

y = np.dot(A,R)
print ('y =', y)

z = x - y
print ('z =', z)
s = np.dot(z,y)
print ('s =', s)