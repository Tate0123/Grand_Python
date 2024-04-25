x = int(input('Ввести число x'))
y = int(input('Ввести число y'))
z = int(input('Ввести число z'))
r1 = max(x, y, z)
if r1 // 2:
    print('Число четное')
else:
    print('Число не четное')