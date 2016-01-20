#!/usr/bin/env python

#FilterByTaxon by Keith Yamada (20.1.2016)
#Usage FilterByTaxon.py INPUT.txt OUTPUT_good.txt OUTPUT_bad.txt TAXONS_LIST.txt

# Takes Blast file with columns: query name, accession, subject name, taxonomy, hsp expect
# Separates out given taxonomy information


import sys

IN = open(sys.argv[1],'r')
OUT_good = open(sys.argv[2],'w')
OUT_bad = open(sys.argv[3],'w')
LIST = open(sys.argv[4],'r').readlines()

headers = IN.readline() # write headers to out files
OUT_good.write(headers)
OUT_bad.write(headers)

lines = IN.readlines()
for line in lines:
    found = 0
    tax = line.split('\t')[3]
    for i in LIST:
        if tax.find(i.strip()) != -1: # if genus from list is found
            found += 1 # add 1 to found
        else:
            continue # else continue down the list
    if found == 0 : # if none from list are found
        OUT_good.write(line) # write to good
    else:
        OUT_bad.write(line) # else write to bad


OUT_good.close()
OUT_bad.close()












        
        
