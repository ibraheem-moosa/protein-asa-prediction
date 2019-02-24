from regression import *
from sklearn.ensemble import GradientBoostingRegressor
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
    gbt = GradientBoostingRegressor(max_depth=12, loss='lad',
                                    n_estimators=10000, verbose=5,
                                    n_iter_no_change=5, learning_rate=0.1)
    do_cross_validation(gbt, data_dir, ws, train_ratio, cv)
