#!/usr/bin/env python

#GroupTaxon by Keith Yamada (8.2.2016)
#Usage AddAno.py pannzer.DE blastx.txt OUTPUT.txt

# Takes Blastx2nr and Pannzer annotations as input
# Groups annotations into a venn diagram style (Pannzer only, Both, Blastx only)


import sys

Pan = open(sys.argv[1],'r')
Bla = open(sys.argv[2],'r')
OUT = open(sys.argv[3],'w')

Pan.readline() #remove column headers
Bla.readline()

# Get pannzer query IDs
pan_ids = []
lines = Pan.readlines()
for line in lines:
    pan_ids.append(line.split('|')[0])
pan_set = set(pan_ids) # convert to set (discovered Pannzer can give more than 1 annotation per contig)

# Get blastx query IDs
bla_ids = []
lines = Bla.readlines()
for line in lines:
    bla_ids.append(line.split('\t')[0])
bla_set = set(bla_ids) # convert to set



# Group
id_set = pan_set.union(bla_set)

both = pan_set.intersection(bla_set)
pan_only = pan_set.difference(bla_set)
bla_only = bla_set.difference(pan_set)


# write to output
OUT.write('Pannzer Only: '+ str(len(pan_only)))
OUT.write('\nBlastX Only: '+ str(len(bla_only)-1)) # for blastx some IDs are '-'
OUT.write('\nBoth: '+ str(len(both)))
OUT.write('\nTotal Annotated Contigs: '+ str(len(id_set)-1)) # -1 to remove '-' ID



OUT.close()












        
        
