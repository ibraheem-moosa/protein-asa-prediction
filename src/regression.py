from load_oh import *
from load_non_oh import *
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score


def load_data(oh, data_dir, ws, y_transform=None):
    if oh:
        load_func = load_oh
    else:
        load_func = load_non_oh
    X, y, test_X, test_y = load_func(data_dir, ws)
    if y_transform is not None:
        y = y_transform(y)
        test_y = y_transform(test_y)
    return X, y, test_X, test_y


def do_fit(reg, data_dir, ws, train_ratio,
           cv, oh=False, y_transform=None, y_rev_transform=None):
    X, y, test_X, test_y = load_data(oh, data_dir, ws, y_transform)
    print('Dataset loaded')
    print('Calling fit')
    reg.fit(X, y)
    test_y_pred = reg.predict(test_X)
    if y_rev_transform is not None:
        test_y_pred = y_rev_transform(test_y_pred)
        test_y = y_rev_transform(test_y)
    print(mean_absolute_error(test_y, test_y_pred))
    return reg


def do_cross_validation(reg, data_dir, ws, train_ratio,
                        cv, oh=False, y_transform=None, y_rev_transform=None):
    X, y, test_X, test_y = load_data(oh, data_dir, ws, y_transform)
    print('Dataset loaded')
    print('Doing {}-fold cross validation'.format(cv))
    if y_rev_transform is not None:
        scorer = make_scorer(lambda y, y_pred:
                             mean_absolute_error(y_rev_transform(y),
                                                 y_rev_transform(y_pred)))
    else:
        scorer = make_scorer(mean_absolute_error)

    cv_result = cross_val_score(reg, X, y, cv=cv,
                                scoring=scorer,
                                verbose=100, n_jobs=1)
    print(cv_result)
    print(cv_result.mean())
    return cv_result
