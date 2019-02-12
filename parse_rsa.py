# coding: utf-8
from Bio.PDB import Polypeptide

def parse_rsa(fname):
    aa = []
    asa = []
    with open(fname) as f:
        ignore_line = 2
        for line in f:
            if ignore_line > 0:
                ignore_line -= 1
                continue
            line = line.split()
            aa.append(Polypeptide.one_to_index(line[1]))
            asa.append(float(line[2]))
    return aa, asa
    
    
            
            
            
