import matplotlib.pyplot as plt
import numpy as np


def plot_uav_data():
    t = []
    no2 = []
    x = []
    y = []
    with open('UAV_data.txt', 'r') as source:
        next(source)
        lines = source.readlines()
    for i in range(len(lines)):
        data = lines[i].split('\t')
        t += [int(data[0])]
        no2 += [float(data[1])]
        x += [float(data[2])]
        y += [float(data[3])]
    t2 = np.array(t)
    no2_2 = np.array(no2)
    x1 = np.array(x)
    y1 = np.array(y)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(x1, y1)
    ax2.plot(t2, no2_2, color='red')
    ax1.set_title('Flight path of UAV')
    ax2.set_title('No2 Conc')
    ax1.set(xlabel='x-coord', ylabel='y-coord')
    ax2.set(xlabel='Time', ylabel='No2 Conc')

    plt.show()


if __name__ == '__main__':
    plot_uav_data()

