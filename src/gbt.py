from load_non_oh import *
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
import numpy as np
import sys

if __name__ == '__main__':

    random.seed(42)
    np.random.seed(42)

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    train_prot_windows, train_asas, test_prot_windows, test_asas = load_non_oh(data_dir, ws)
    print('Dataset loaded')
    gbt = GradientBoostingRegressor(max_depth=12, loss='lad', n_estimators=10000, verbose=5, n_iter_no_change=5, learning_rate=0.1)
    print('Doing 5-fold cross validation')
    cv_result = cross_val_score(gbt, train_prot_windows, train_asas, cv=5, scoring=make_scorer(mean_absolute_error), verbose=100, n_jobs=1)
    print(cv_result)
    print(cv_result.mean())

    print('Calling fit')
    gbt.fit(train_prot_windows, train_asas)
    print(mean_absolute_error(test_asas, gbt.predict(test_prot_windows)))
