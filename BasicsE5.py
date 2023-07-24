# Drawing 3D scatter graph of acceleration data

import matplotlib.pyplot as plt


def read_f(f_name):
    with open(f_name, mode="r") as file:
        acceleration_list = [list(map(lambda x: round(float(x), 2), line.split(",")[4:7]))
                             for line in file.readlines()[1:]]
    return acceleration_list


def split_list(list_, index):
    count = 0
    result = []
    for list_of_list in list_:
        if count == 100:
            break
        result.append(list_of_list[index])
        count += 1
    return result


def plot_waveform(list_x, list_y, list_z):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    sc = ax1.scatter(list_x, list_y, list_z)
    plt.colorbar(sc)
    plt.show()


if __name__ == "__main__":
    acc_list = read_f("./sample.csv")
    acc_x = split_list(acc_list, 0)
    acc_y = split_list(acc_list, 1)
    acc_z = split_list(acc_list, 2)
    plot_waveform(acc_x, acc_y, acc_z)
