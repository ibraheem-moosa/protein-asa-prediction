from parse_rsa import *
from split_train_test import *
import os
import torch

def load_torch_as_seq(data_dir, train_ratio=0.8):
    proteins = []
    asas = []
    files = os.listdir(data_dir)
    for fname in files:
        protein, asa = parse_rsa(os.path.join(data_dir, fname))
        protein = list(map(noh_to_oh, protein))
        proteins.append(protein)
        asas.append(asa)
    train_proteins, train_asas, test_proteins, test_asas = split_train_test_without_chaining(proteins, asas, train_ratio)


