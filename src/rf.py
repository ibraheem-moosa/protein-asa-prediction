from regression import *
from sklearn.ensemble import RandomForestRegressor
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
    rf = RandomForestRegressor(max_depth=30, n_estimators=100, verbose=10)
    do_cross_validation(rf, data_dir, ws, train_ratio, cv,
                        y_transform=np.sqrt, y_rev_transform=np.square)
