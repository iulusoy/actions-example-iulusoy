import numpy as np


def example_function():
    array = np.zeros(3)
    array2 = np.ones(3)

    for i in range(0, 3):
        array[i] = i**2
        array2[i] = i / 2

    return array, array2

print(example_function())
