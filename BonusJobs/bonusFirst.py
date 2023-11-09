import scipy
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def bonusJob():
    samples = [1, 10, 100, 1000]
    means = []

    for i in samples:
        np.random.seed(1)
        x = [np.mean(np.random.randint(1, 7, i)) for _ in range(1000)]
        means.append(x)

    k = 0

    fig, ax = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(0, 2):
        for j in range(0, 2):
            ax[i, j].hist(means[k], 10, density=True)
            ax[i, j].set_title("n = {}".format(samples[k]))
            k += 1
            
    plt.show()