import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
y = np.sin(x)

f1, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
ax.set_xlabel('x label')
ax.set_ylabel('y label')

x = np.linspace(0, 2, 100)

f2, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()


f3, (ay1, ay2) = plt.subplots(2, 1)
ay1.plot(x, y)
ay1.set_title('Sharing X axis')
ay2.scatter(x, y, marker='.')


kw = {'xticks': [0, 2, 4, 6], 'yticks': [0.2, 0.4, 0.6, 0.8]}
f4, axs = plt.subplots(2, 2, subplot_kw=kw)
axs[0, 0].plot(x, y)
axs[1, 0].scatter(x, y, marker='*')
axs[0, 1].scatter(x, y, marker='1')
axs[1, 1].scatter(x, y)

plt.show()
