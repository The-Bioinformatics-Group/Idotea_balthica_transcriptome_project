# Idotea_balthica_transcriptome_project

###This repository will be the storage place for statistics/data concerning the Idotea balthica transcriptome assembly project.

I will follow the 'best practice' pipeline fron the paper, SNP genotyping and population genomics from expressed sequences -current advances and future possibilities (De Wit et. al. 2015).
All analysis will be done on the Taito supercluster at CSC.


# Preprocessing
1. Visualize with FASTQC
2. Trim adapters and low quality with TRIMMOMATIC
3. Error correct with RCORRECTOR
4. In silico normalization built into TRINITY


# De novo Assembly
Using TRINITY (20/25/30mers)
Clustering using CD-HIT


# Quality Evaluation / Optimization
1. Quality evaluation and filtering with TRANSRATE
2. Assess the completeness using BUSCO
3. Find ORFs and generate protein sequences with TRANSDECODER


# Annotation 
Using PANNZER
BLASTX to nr
