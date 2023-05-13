# Ce code présente animation simple pour présenter la régression linéaire.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.animation import FuncAnimation

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

x = []
y = []

def create_pseudo_random_data(x):
    variation = np.random.randint(-6, 6)
    y = 2 * x + 1 + variation
    return y

def animate(i):
    # on place des points aléatoires mais continue en x
    previous_x = x[-1] if len(x) > 0 else 0
    x.append(previous_x + 1)
    y.append(create_pseudo_random_data(x[-1]))
    # on affiche les points (on ne relie pas les points)
    ax1.clear()
    ax1.scatter(x, y)
    if len(x) > 2:
        # on calcule la régression linéaire
        moyenne_x = np.mean(x)
        moyenne_y = np.mean(y)
        moyenne_x_carre = np.mean([x_i * x_i for x_i in x])




        moyenne_xy = np.mean([x_i * y_i for x_i, y_i in zip(x, y)])
        # on calcule les coefficients de la droite
        a = (moyenne_xy - moyenne_x * moyenne_y) / (moyenne_x_carre - moyenne_x * moyenne_x)
        b = moyenne_y - a * moyenne_x
        print('a =', a, 'b =', b)
        # on affiche la droite
        x_min = min(x)
        x_max = max(x)
        y_min = a * x_min + b
        y_max = a * x_max + b
        ax1.plot([x_min, x_max], [y_min, y_max], color='red')
ani = FuncAnimation(fig, animate, interval=1000)
plt.show()