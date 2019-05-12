from scipy.optimize import fmin
import numpy as np


def f(x):
    return x ** 2 - 4 * x + 8


print(fmin(f, 1))
