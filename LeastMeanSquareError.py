# Draws approximate linear lines using data from sample.csv

import numpy as np
import matplotlib.pyplot as plt


def read_f(f_name):
    with open(f_name, mode="r") as file:
        acceleration_list = [list(map(lambda x: round(float(x), 2), line.split(",")[7:10]))
                             for line in file.readlines()[1:]]
    return acceleration_list


def split_list(list_, index):
    result = []
    for list_of_list in list_:
        result.append(list_of_list[index])
    return np.array(result)


def reg1dim(x, y):
    n = len(x)
    gradiant = ((np.dot(x, y) - y.sum() * x.sum()/n) / ((x ** 2).sum() - x.sum()**2 / n))
    offset = (y.sum() - gradiant * x.sum())/n
    return gradiant, offset


def plot_scatter(x_axe, y_axe):
    a, b = reg1dim(x_axe, y_axe)
    plt.scatter(x_axe, y_axe)
    plt.plot([0, x_axe.max(initial=0)], [b, a * x_axe.max(initial=0) + b])


acc_list = read_f("./sample.csv")
x_list = split_list(acc_list, 0)
y_list = split_list(acc_list, 1)
z_list = split_list(acc_list, 2)
time = np.linspace(0, 5114, 5114)

plot_scatter(time, x_list)
plot_scatter(time, y_list)
plot_scatter(time, z_list)

plt.show()
