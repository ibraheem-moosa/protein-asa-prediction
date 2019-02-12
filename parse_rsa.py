# coding: utf-8
from Bio.PDB import Polypeptide

def parse_rsa(fname):
    protein = []
    asa = []
    with open(fname) as f:
        ignore_line = 2
        for line in f:
            if ignore_line > 0:
                ignore_line -= 1
                continue
            line = line.split()
            protein.append(Polypeptide.one_to_index(line[1]))
            asa.append(float(line[2]))
    return protein, asa
    
    
            
            
            
