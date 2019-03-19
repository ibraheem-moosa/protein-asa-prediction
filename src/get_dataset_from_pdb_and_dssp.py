import os
import sys
from tqdm import tqdm
from Bio.PDB import MMCIFParser
from Bio.PDB.DSSP import make_dssp_dict

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: python {} protein_list pdb_dir dssp_dir out_dir'
              .format(sys.argv[0]))
        exit()

    protein_list_file = sys.argv[1]
    with open(protein_list_file) as f:
        protein_list = [l.strip() for l in f]
    mmcif_parser = MMCIFParser()
    pdb_dir = sys.argv[2]
    dssp_dir = sys.argv[3]
    out_dir = sys.argv[4]
    for pdb_id in tqdm(protein_list):
        pdb_fname = os.path.join(pdb_dir, pdb_id + '.cif')
        dssp_fname = os.path.join(dssp_dir, pdb_id + '.dssp')
        if not os.path.exists(pdb_fname):
            continue
        if not os.path.exists(dssp_fname):
            continue
        try:
            s = mmcif_parser.get_structure('X', pdb_fname)
        except Exception as e:
            print(e)
            print(pdb_id)
            continue
        try:
            d = make_dssp_dict(dssp_fname)
        except Exception as e:
            print(e)
            print(pdb_id)
            continue
        out_fname = os.path.join(out_dir, pdb_id + '.output')
        with open(out_fname, 'w') as f:
            for residue in s.get_residues():
                chain = residue.get_full_id()[2]
                if residue.get_full_id()[2:] in d[0]:
                    dssp_result = d[0][residue.get_full_id()[2:]]
                    resname = residue.resname  # dssp_result[0]
                    ss = dssp_result[1]
                    asa = dssp_result[2]
                    phi = dssp_result[3]
                    psi = dssp_result[4]
                    out_line = '{} {} {} {} {} {}'.format(
                        chain, resname, ss, asa, phi, psi)
                    for atom in residue.get_atoms():
                        out_line += ' {} {}'.format(atom.name, atom.bfactor)
                    f.write(out_line + '\n')
