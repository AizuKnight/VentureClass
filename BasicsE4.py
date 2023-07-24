# Drawing the waveform of acceleration data

import matplotlib.pyplot as plt
import numpy as np


def read_f(f_name):
    with open(f_name, mode="r") as file:
        acceleration_list = [list(map(lambda x: round(float(x), 2), line.split(",")[4:7]))
                             for line in file.readlines()[1:]]
    return acceleration_list


def split_list(list_, index):
    result = []
    for list_of_list in list_:
        result.append(list_of_list[index])
    return result


def plot_waveform(list_x, list_y, list_z):
    x = np.linspace(0, 5114, 5114)
    fig, ax = plt.subplots()
    ax.plot(x, list_x, label="x-acc")
    ax.plot(x, list_y, label="y-acc")
    ax.plot(x, list_z, label="z-acc")
    ax.set_xlabel("Time?")
    ax.set_ylabel("Acceleration Value")
    ax.set_title("Acceleration Transition")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    acc_list = read_f("./sample.csv")
    acc_x = split_list(acc_list, 0)
    acc_y = split_list(acc_list, 1)
    acc_z = split_list(acc_list, 2)
    plot_waveform(acc_x, acc_y, acc_z)
