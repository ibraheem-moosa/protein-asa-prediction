import random
from itertools import chain

def split_train_test(aas, asas, train_ratio):
    indices = list(range(len(aas)))
    random.shuffle(indices)
    train_indices = indices[:int(0.8 * len(indices))]
    test_indices = indices[int(0.8 * len(indices)):] 
    train_aas = [aas[i] for i in train_indices]
    train_asas = [asas[i] for i in train_indices]
    test_aas = [aas[i] for i in test_indices]
    test_asas = [asas[i] for i in test_indices]
    train_aas = list(chain(*train_aas))
    train_asas = list(chain(*train_asas))
    test_aas = list(chain(*test_aas))
    test_asas = list(chain(*test_asas))
    return train_aas, train_asas, test_aas, test_asas


