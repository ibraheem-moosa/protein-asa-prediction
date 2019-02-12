from parse_rsa import *
from transform_input import *
from split_train_test import *
import os

def load_non_oh(data_dir, ws, train_ratio=0.8):
    aas = []
    asas = []
    files = os.listdir(data_dir)
    for fname in files:
        aa, asa = parse_rsa(os.path.join(data_dir, fname))
        aa = transform_input(aa, ws)
        aas.append(aa)
        asas.append(asa)
    return split_train_test(aas, asas, train_ratio)

