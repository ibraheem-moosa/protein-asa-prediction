from load_oh import *
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    train_prot_windows, train_asas, test_prot_windows, test_asas = load_oh(data_dir, ws)
    print('Dataset loaded')
    print('Doing Random Grid Search with  5-fold cross validation')
    mlp = MLPRegressor(verbose=True, early_stopping=True)
    param_distributions = {'learning_rate_init':10.0**np.arange(-5,0), 
                            'n_iter_no_change':list(range(2,20,2)), 
                            'alpha':10.0**np.arange(-3,3),
                            'beta_1':1 - 10.0**np.arange(-3, 0),
                            'beta_2':1 - 10.0**np.arange(-6, -3)}
    rscv = RandomizedSearchCV(mlp, param_distributions, n_iter=25, scoring=make_scorer(mean_absolute_error), cv=5, verbose=100, return_train_score=True) 
    rscv.fit(train_prot_windows, train_asas)
    #mlp = MLPRegressor(hidden_layer_sizes=(100,), verbose=True, early_stopping=True, learning_rate_init=0.01, alpha=1, n_iter_no_change=20)
    #print('Doing 5-fold cross validation')
    #cv_result = cross_val_score(mlp, train_prot_windows, train_asas, cv=5, scoring=make_scorer(mean_absolute_error), verbose=100, n_jobs=1)
    #print(cv_result)
    #print(cv_result.mean())
    #print('Calling fit')
    #mlp.verbose = False
    #mlp.fit(train_prot_windows, train_asas)
    print(mean_absolute_error(test_asas, rscv.predict(test_prot_windows)))
    with open('rscv-output', 'w') as f:
        f.write(str(rscv.cv_results_))
        f.write('\n')
        f.write(str(rscv.best_params_))
        f.write('\n')
        f.write(str(rscv.best_score_))
        f.write('\n')
        f.write(str(rscv.refit_time_))

