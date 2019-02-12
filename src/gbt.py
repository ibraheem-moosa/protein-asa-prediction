from load_non_oh import *
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    train_prot_windows, train_asas, test_prot_windows, test_asas = load_non_oh(data_dir, ws)
    gbt = GradientBoostingRegressor(max_depth=3, n_estimators=1000, verbose=5, n_iter_no_change=5)
    gbt.fit(train_prot_windows, train_asas)
    print(mean_absolute_error(test_asas, gbt.predict(test_prot_windows)))
