# coding: utf-8
def transform_input(aas, ws):
    t_aas = []
    for i in range(len(aas)):
        start = max(0, i - ws)
        end = min(i + ws + 1, len(aas) - 1)
        w = (start - (i - ws)) * [21] +  aas[start:end] + (i + ws + 1 - end) * [21]
        assert(len(w) == 2 * ws + 1)
        t_aas.append(w)
    return t_aas
    
