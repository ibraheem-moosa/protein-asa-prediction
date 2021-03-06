import random
from itertools import chain

def split_train_test_without_chaining(proteins, asas, train_ratio):
    indices = list(range(len(proteins)))
    random.shuffle(indices)
    train_indices = indices[:int(train_ratio * len(indices))]
    test_indices = indices[int(train_ratio * len(indices)):] 
    train_proteins = [proteins[i] for i in train_indices]
    train_asas = [asas[i] for i in train_indices]
    test_proteins = [proteins[i] for i in test_indices]
    test_asas = [asas[i] for i in test_indices]
    return train_proteins, train_asas, test_proteins, test_asas


def split_train_test(proteins, asas, train_ratio):
    train_proteins, train_asas, test_proteins, test_asas = split_train_test_without_chaining(proteins, asas, train_ratio)
    train_proteins = list(chain(*train_proteins))
    train_asas = list(chain(*train_asas))
    test_proteins = list(chain(*test_proteins))
    test_asas = list(chain(*test_asas))
    return train_proteins, train_asas, test_proteins, test_asas

