import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 100
    X = np.random.rand(N, 3)
    y = np.random.rand(N) * 2 - 1
    print(y)

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    sc = ax1.scatter(X[:, 0], X[:, 1], zs=X[:, 2], zdir='z', s=50, vmin=0, vmax=1, c=y, cmap=plt.cm.jet)
    plt.colorbar(sc)

    plt.show()
