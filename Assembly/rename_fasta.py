### Created: 7 Oct 2015
### Replaces header with #/1 or #/2
### e.g. python rename_fasta.py out_fw_corrected.fa /1 left.fa

import sys

first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]

def rename(file1=first_arg, end=second_arg, out=third_arg):

    fasta = open(file1,'r')
    newfasta = open(out, 'w')

    n = 0

    for line in fasta:
        if line.startswith('>'):
            newname = '>' + str(n) + end + '\n'
            n += 1
            newfasta.write(newname)
        else:
            newfasta.write(line)

    fasta.close()
    newfasta.close()

if __name__ == "__main__":
    rename()
