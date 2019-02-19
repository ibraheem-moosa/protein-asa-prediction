from load_non_oh import *
from catboost import Pool, CatBoostRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
import sys
import numpy as np

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
    train_pool = Pool(train_prot_windows, train_asas, cat_features=list(range(len(train_prot_windows[0]))))
    test_pool = Pool(test_prot_windows, test_asas, cat_features=list(range(len(test_prot_windows[0]))))
    cbt = CatBoostRegressor(depth=3, loss_function='MAE')
    '''
    print('Doing 5-fold cross validation')
    cv_result = cross_val_score(gbt, train_prot_windows, train_asas, cv=5, scoring=make_scorer(mean_absolute_error), verbose=100, n_jobs=1)
    print(cv_result)
    print(cv_result.mean())
    '''
    print('Calling fit')
    cbt.fit(train_pool)
    print(mean_absolute_error(test_asas, cbt.predict(test_pool)))

