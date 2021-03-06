from load_non_oh import *
from catboost import Pool, CatBoostRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from regression import *
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
    cv = 5
    train_ratio = 0.8
    #train_prot_windows, train_asas, test_prot_windows, test_asas = load_non_oh(data_dir, ws)
    print('Dataset loaded')
    #train_pool = Pool(train_prot_windows, train_asas, cat_features=list(range(len(train_prot_windows[0]))))
    #test_pool = Pool(test_prot_windows, test_asas, cat_features=list(range(len(test_prot_windows[0]))))
    params = {
            'depth': range(10,17),
            'learning_rate': 10.0**np.arange(-1,1),
            'bagging_temparature':[0,1],
            #'rsm':np.arange(0.1,1.,.3),
            'l2_leaf_reg':[1,2,3],
            'random_strength':np.arange(0.,1.,.2)}

    cbt = CatBoostRegressor(loss_function='RMSE', learning_rate=1.0,
            depth=8, n_estimators=10000,
            cat_features=list(range(2 * ws + 1)), task_type='CPU')
    do_cross_validation(cbt, data_dir, ws, train_ratio, cv,
                        y_transform=np.sqrt, y_rev_transform=np.square)
    exit()
    rscv = RandomizedSearchCV(cbt, params, n_iter=32, scoring='neg_mean_absolute_error', cv=5, verbose=10)
    '''
    print('Doing 5-fold cross validation')
    cv_result = cross_val_score(gbt, train_prot_windows, train_asas, cv=5, scoring=make_scorer(mean_absolute_error), verbose=100, n_jobs=1)
    print(cv_result)
    print(cv_result.mean())
    '''
    print('Calling fit')
    rscv.fit(train_prot_windows, train_asas)
    print('Running on test set')
    print(mean_absolute_error(test_asas, cbt.predict(test_prot_windows)))
    print('Dumping cv results')
    print(rscv.cv_results_)
    print(rscv.best_score_)
    print(rscv.best_params_)

