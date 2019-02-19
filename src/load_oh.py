from parse_rsa import *
from transform_input import *
from split_train_test import *
import os
from itertools import chain

def load_oh(data_dir, ws, train_ratio=0.8):
    proteins = []
    asas = []
    files = os.listdir(data_dir)
    for fname in files:
        protein, asa = parse_rsa(os.path.join(data_dir, fname))
        protein = windows_from_seq(protein, ws)
        protein = list(map(noh_to_oh, protein))
        proteins.append(protein)
        asas.append(asa)
    return split_train_test(proteins, asas, train_ratio)

