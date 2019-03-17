import os
import sys


def run_mkdssp(input_file, output_dir):
    pdb_id = os.path.basename(os.path.normpath(input_file)).rsplit('.')[0]
    output_file = os.path.join(output_dir, pdb_id + '.dssp')
    if os.path.exists(output_file):
        print('Skipping {}'.format(pdb_id))
        return 0
    print(output_file)
    print('Running mkdssp for {}'.format(input_file))
    return os.system('mkdssp -i {} -o {}'.format(input_file, output_file))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python run_mkdssp.py input_dir, output_dir')
        exit()
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    for input_file in os.listdir(input_dir):
        if input_file.endswith('.cif') or input_file.endswith('.pdb'):
            run_mkdssp(os.path.join(input_dir, input_file), output_dir)
