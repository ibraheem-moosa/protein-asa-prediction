from regression import *
from sklearn.tree import DecisionTreeRegressor
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
    dt = DecisionTreeRegressor(max_depth=1, criterion='mae')
    do_cross_validation(dt, data_dir, ws, train_ratio, cv,
                        y_transform=np.sqrt, y_rev_transform=np.square)
