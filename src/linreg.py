from load_oh import *
from sklearn.linear_model import LinearRegression
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
    train_prot_windows, train_asas, test_prot_windows, test_asas = load_oh(data_dir, ws)
    print('Dataset loaded')
    linreg = LinearRegression()
    print('Doing 5-fold cross validation')
    cv_result = cross_val_score(linreg, train_prot_windows, train_asas, cv=5, scoring=make_scorer(mean_absolute_error), verbose=100)
    print(cv_result)
    print(cv_result.mean())

    print('Calling fit')
    linreg.fit(train_prot_windows, train_asas)
    print(mean_absolute_error(test_asas, linreg.predict(test_prot_windows)))
