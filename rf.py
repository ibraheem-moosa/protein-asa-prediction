from load_non_oh import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    train_aas, train_asas, test_aas, test_asas = load_non_oh(data_dir, ws)
    rf = RandomForestRegressor(max_depth=4, n_estimators=100)
    rf.fit(train_aas, train_asas)
    print(mean_absolute_error(test_asas, rf.predict(test_aas)))
