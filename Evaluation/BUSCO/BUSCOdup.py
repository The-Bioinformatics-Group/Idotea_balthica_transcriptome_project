#!/usr/bin/env python

#GroupTaxon by Keith Yamada (5.2.2016)
#Usage BUSCOdup.py INPUT.txt OUTPUT.txt

# Takes BUSCO full table file with columns: BUSCO_group, Status, Transcript, Bitscore, Length
# Identifies how many times a duplicated BUSCO is duplicated


import sys

IN = open(sys.argv[1],'r')
OUT = open(sys.argv[2],'w')

headers = IN.readline() 

# extract duplicated BUSCOs
dups = []
lines = IN.readlines()
for line in lines: # for each line
    status = line.split('\t')[1] # identify the status
    if status == 'Duplicated': # if the status is 'Duplicated'
        dups.append(line) # add that line to the dups list


# group by BUSCO_group
groups = {}
for dup in dups: # for each duplicate
    BUSCO = dup.split('\t')[0] # identify the BUSCO
    if groups.has_key(BUSCO): # if the BUSCO is already in the dictionary
        groups[BUSCO] += 1 # increase value by 1
    else: # else BUSCO is not in the dictionary
        groups[BUSCO] = 1 # add BUSCO to the dictionary

order = sorted(groups.items(), key=lambda x:x[1], reverse=True)
for i in order:
    OUT.write(i[0]+'\t'+'#'+str(i[1])+'\n')


OUT.close()












        
        
