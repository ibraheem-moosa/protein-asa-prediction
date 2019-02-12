from load_oh import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: python _ data_dir ws')
        exit()

    data_dir = sys.argv[1]
    ws = int(sys.argv[2])
    train_prot_windows, train_asas, test_prot_windows, test_asas = load_oh(data_dir, ws)
    linreg = LinearRegression()
    linreg.fit(train_prot_windows, train_asas)
    print(mean_absolute_error(test_asas, linreg.predict(test_prot_windows)))
