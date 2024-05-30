import numpy as np
import matplotlib.pyplot as plt
# функция
y = lambda x: 2*(x**4) - 21*(x**3) + 20*x - 3
print("y:", y)

# создаѐм область, в которой будет
# - отображаться график
x = np.linspace(-5, 5, 42)
xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')

fmax = max(y(x))
print('Ymax = ',fmax)

xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')

fmin = min(y(x))
print('Ymin = ',fmin)

fig = plt.subplots()

plt.plot(x, y(x))

plt.show()