# coding: utf-8
from itertools import chain

'''
Create windows from protein sequence
'''
def windows_from_seq(aas, ws):
    t_aas = []
    for i in range(len(aas)):
        start = max(0, i - ws)
        end = min(i + ws + 1, len(aas) - 1)
        w = (start - (i - ws)) * [21] +  aas[start:end] + (i + ws + 1 - end) * [21]
        assert(len(w) == 2 * ws + 1)
        t_aas.append(w)
    return t_aas

def noh_to_oh(protein):
    protein = list(map(lambda aa:[1 if i==aa else 0 for i in range(21)], protein))
    protein = list(chain(*protein))
    return protein

   
