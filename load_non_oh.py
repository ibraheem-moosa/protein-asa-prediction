from parse_rsa import *
from transform_input import *
from split_train_test import *
import os

def load_non_oh(data_dir, ws, train_ratio=0.8):
    proteins = []
    asas = []
    files = os.listdir(data_dir)
    for fname in files:
        protein, asa = parse_rsa(os.path.join(data_dir, fname))
        protein = transform_input(protein, ws)
        proteins.append(protein)
        asas.append(asa)
    return split_train_test(proteins, asas, train_ratio)

