# Python Bioinformatics Tools Overview
This repository contains a collection of Python scripts and tools for common bioinformatics tasks, including sequence filtering, alignment summarization and counts, variant file comparison, conversions, and more.

These tools are designed for flexibility, command-line usage, and integration into larger bioinformatics workflows.

#  Datasets

Data used in these tools are derived from synthetic data in order to perform different bioinformatics analyses. 

Any SNP related analyses utilized "The Breast and Prostate Cancer Cohort Consortium (BPC3) GWAS of Aggressive Prostate Cancer and ER- Breast Cancer"​

dbGaP Study Accession: phs00081vp1; (https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/analysis.cgi?study_id=phs00081vp1&phv=217909&phd=&pha=3864&pht=4297&phvf=&phdf=&phaf=&phtf=&dssp=1&consent=&temp=1 )

# Data Preprocessing Folder

Converts .chpa file to .vcf format

'''python
##fileformat=VCFv4.2
#CHROM  POS  ID  REF  ALT  QUAL  FILTER  INFO
chr1    123456  .  A  G  .  .  .
chr2    234567  .  T  C  .  .  .'''
