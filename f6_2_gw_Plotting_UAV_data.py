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
        t += lines[i][0]
        no2 += lines[i][1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(t, no2)

    plt.show()


    return 0

plot_uav_data()