from regression import *
from sklearn.linear_model import LinearRegression
import numpy as np
import random
import sys

if __name__ == '__main__':

    random.seed(42)
    np.random.seed(42)

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    cv = 5
    train_ratio = 0.8
    linreg = LinearRegression()
    do_cross_validation(linreg, data_dir, ws, train_ratio, cv)
