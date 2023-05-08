import matplotlib.pyplot as plt
import numpy as np


# plot histogram function
def plot_histogram(data):
    low = min(data) - .5
    high = max(data) + .5
    nr_of_bins = max(data) - min(data) + 2  # number of bins
    bbb = np.linspace(low, high, nr_of_bins)
    plt.hist(data, bbb)
    plt.show()


if __name__ == '__main__':
    example_list = [9, 18, 13, 9, 6, 6, 16, 6, 17, 10, 15, 16, 13, 11, 13, 8, 20, 6, 18, 11]
    plot_histogram(np.array(example_list))
