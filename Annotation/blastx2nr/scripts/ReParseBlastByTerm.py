#!/usr/bin/env python

#ReParseBlastByTerm by Keith Yamada (19.1.2016)
#Usage ReParseBlastByTerm.py INPUT.txt OUTPUT.txt OUTPUT_terms.txt TERMS(comma separated and lowercase)

# Takes Blast file with columns: query name, accession, subject name, taxonomy, hsp expect
# Finds TERMS (e.g. predicted, hypothetical) and removes them to a separate file


import sys

IN = open(sys.argv[1],'r')
OUT = open(sys.argv[2],'w')
OUT_terms = open(sys.argv[3],'w')
TERMS = sys.argv[4].split(',')

header = IN.readline()
OUT.write(header) # write column names to output file
OUT_terms.write(header)

lines = IN.readlines()
for line in lines:
    col = line.split('\t')
    count = 0
    for term in TERMS:
        if col[2].find(term) != -1 or col[2].find(term.capitalize()) != -1 or col[2].find(term.upper()) != -1: # if term found
            count += 1 # increase count
    if count == 0: # if no terms found
        OUT.write(line)
    else:
        OUT_terms.write(line)
        
    


OUT.close()












        
        
