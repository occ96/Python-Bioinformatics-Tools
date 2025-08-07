# Purpose: To convert .chpa files to .vcf format

import pandas as pd

# File path, modify as needed with actual path
chpa_file = "pha003864.v1.p1.chr21.chpa" # Input file
vcf_file = "output.vcf" # Output .vcf

# Read the .chpa file, skipping metadata lines beginning with "#"
df = pd.read_csv(chpa_file, sep="\t", comment="#", low_memory=False)

# Select and  rename relevant columns for VCF final format
vcf_df = df[['Chr ID', 'Chr Position', 'SNP ID', 'Allele1', 'Allele2']].copy()
vcf_df.columns = ['#CHROM', 'POS', 'ID', 'REF', 'ALT'] #Rename to VCF format

# Add required VCF fields
vcf_df['QUAL'] = '.' # Placeholder for Quality score
vcf_df['FILTER'] = 'PASS' # Default filter status

# Construct INFO column with aditional details (P-value, odds radio, CI)
vcf_df['INFO'] = (
    "PVAL=" + df['P-value'].astype(str) +
    ";OR=" + df['Odds Ratio'].astype(str) +
    ";CI_LOW=" + df['CI Low'].astype(str) +
    ";CI_HIGH" + df['CI High'].astype(str)
)

# VCF File Header
vcf_header = """##fileformat=VCFv4.2
##source=CHPA_to_VCF_Converter
##reference=CRCh38
##INFO=<ID=PVAL,Number=1, Type=Float,Description="P-value from GWAD analysis">
##INFO=<ID=OR,Number=1,Type=Float, Description="Odds Ratio">
##INFO=<ID=CI_LOW,Number=1, Type=Float, Description="Lower bound of Confidence Interval">
##INFO=<ID=CI_HIGH,Number=1, Type=Float, Description="Upper bound of Confidence Interval">
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"""

# Save as VCF
with open(vcf_file, "w") as f:
    f.write(vcf_header + "\n") # Write VCF header
    vcf_df.to_csv(f, sep="\t", index=False, header=True)

print(f"Conversion complete. Your converted file in .vcf format is saved as {vcf_file}")
