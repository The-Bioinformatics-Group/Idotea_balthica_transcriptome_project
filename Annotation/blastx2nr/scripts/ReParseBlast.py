#!/usr/bin/env python

#ReParseBlast by Keith Yamada (19.1.2016)
#Usage ReParseBlast.py INPUT.txt OUTPUT.txt

# Takes col 0(query name), 2(subject name), 12(HSP expect)
# Outputs as query name, accession, subject name, taxonomy, hsp expect


import sys

IN = open(sys.argv[1],'r')
OUT = open(sys.argv[2],'w')

header = IN.readline()
headers = header.split('\t')
OUT.write(headers[0]+'\t'+'Accession\t'+headers[2]+'\t'+'Taxonomy\t'+headers[12])

lines = IN.readlines()

for line in lines:
    col = line.split('\t')
    n = 0
    for i in range(len(col[2].split('>'))): # annotation loop
        que = col[0].split()[0] # take Trinity header before the first space
        acc = col[2].split('>')[i].split()[0] # takes accession from 'subject name' col
        subject = col[2].split('>')[i].split('|')[4] # subject name + taxon
        sub = subject[1:subject.rfind('[')-1] # subject name
        tax = subject[subject.rfind('[')+1:subject.rfind(']')] # takes taxonomy name from 'subject name' col
        hsp = col[12] # takes hsp (evalue)
        if n == 0: # for first annotation
            OUT.write('\n'+que+'\t'+acc+'\t'+sub+'\t'+tax+'\t'+hsp)
            n += 1
        else: # for additional annotations
            OUT.write('\n'+'-'+'\t'+acc+'\t'+sub+'\t'+tax+'\t'+'-')

OUT.close()












        
        
