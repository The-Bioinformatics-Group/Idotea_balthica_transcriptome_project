#!/usr/bin/env python

#GroupTaxon by Keith Yamada (19.1.2016)
#Usage GroupTaxon.py INPUT.txt OUTPUT.txt

# Takes Blast file with columns: query name, accession, subject name, taxonomy, hsp expect
# Groups taxonomy information


import sys

IN = open(sys.argv[1],'r')
OUT = open(sys.argv[2],'w')

IN.readline() #remove column headers

groups = {}
lines = IN.readlines()
for line in lines:
    tax = line.split('\t')[3]
    if groups.has_key(tax): # if taxon is already in the dictionary
        groups[tax] += 1 # increase value by 1
    else: # else taxon is not in the dictionary
        groups[tax] = 1 # add taxon to the dictionary

order = sorted(groups.items(), key=lambda x:x[1], reverse=True)
for i in order:
    OUT.write(i[0]+'\t'+str(i[1])+'\n')


OUT.close()












        
        
