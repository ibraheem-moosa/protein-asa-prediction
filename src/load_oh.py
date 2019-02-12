from parse_rsa import *
from transform_input import *
from split_train_test import *
import os
from itertools import chain

def window_to_oh(window):
    window = list(map(lambda aa:[1 if i==aa else 0 for i in range(21)], window))
    window = list(chain(*window))
    return window

def load_oh(data_dir, ws, train_ratio=0.8):
    proteins = []
    asas = []
    files = os.listdir(data_dir)
    for fname in files:
        protein, asa = parse_rsa(os.path.join(data_dir, fname))
        protein = transform_input(protein, ws)
        protein = list(map(window_to_oh, protein))
        proteins.append(protein)
        asas.append(asa)
    return split_train_test(proteins, asas, train_ratio)

