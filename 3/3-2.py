f = []
x = int(input('Ввести число x'))
y = int(input('Ввести число y'))
z = int(input('Ввести число z'))
M = int(input('Ввести число M'))
d = [x, y, z]
for a in d:
    if a > M:
        a = a*2
        f.append(a)
print(f, len(f))