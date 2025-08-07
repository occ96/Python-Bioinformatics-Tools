# Purpose: To discover ultra rare variants

import pandas as pd
import glob
import os

# Set directory paths using ANNOVAR data
data_dir = ""
output_dir = ""

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Store results across all chromosomes
all_ultra_rare_exome_snps = []
all_ultra_rare_genome_snps = []

# Define the MAF columns (for both exome and genome)
exome_maf_col = "gnomad41_exome_AF"
genome_maf_col = "gnomad41_genome_AF"

# Find all chromosome files
chromosome_files = glob.glob(os.path.join(data_dir, "output.chr*.csv"))

for file in chromosome_files:
    print(f"Processing {file} ...")
    
    # Load chromosome data
    df = pd.read_csv(file)

    # Convert MAF columns to numeric
    df[exome_maf_col] = pd.to_numeric(df[exome_maf_col], errors='coerce')
    df[genome_maf_col] = pd.to_numeric(df[genome_maf_col], errors='coerce')

    # Drop SNPs with missing MAF values
    df = df.dropna(subset=[exome_maf_col, genome_maf_col])

    # Filter Ultra-Rare SNPs (MAF < 0.1%) for Exome
    ultra_rare_exome_snps = df[df[exome_maf_col] < 0.001]

    # Filter Ultra-Rare SNPs (MAF < 0.1%) for Genome
    ultra_rare_genome_snps = df[df[genome_maf_col] < 0.001]

    # Append results for all chromosomes
    all_ultra_rare_exome_snps.append(ultra_rare_exome_snps)
    all_ultra_rare_genome_snps.append(ultra_rare_genome_snps)

# Combine results from all chromosomes
ultra_rare_exome_snps_df = pd.concat(all_ultra_rare_exome_snps)
ultra_rare_genome_snps_df = pd.concat(all_ultra_rare_genome_snps)

# Save merged results
ultra_rare_exome_snps_df.to_csv(os.path.join(output_dir, "All_Ultra_Rare_SNPs_Exome.csv"), index=False)
ultra_rare_genome_snps_df.to_csv(os.path.join(output_dir, "All_Ultra_Rare_SNPs_Genome.csv"), index=False)

# Print final results
print(f"Processing complete!")
print(f"Ultra-Rare SNPs (Exome): {len(ultra_rare_exome_snps_df)}")
print(f"Ultra-Rare SNPs (Genome): {len(ultra_rare_genome_snps_df)}")

#----------------------------------------------------

#Identify Functionally Impactful Ultra-Rare Variants

# Load ultra-rare SNPs
ultra_rare_exome_snps_df = pd.read_csv("")

# Convert column to string
ultra_rare_exome_snps_df["ExonicFunc.refGeneWithVer"] = ultra_rare_exome_snps_df["ExonicFunc.refGeneWithVer"].astype(str)

# Filter for functional impact
functional_ultra_rare_snps = ultra_rare_exome_snps_df[
    ultra_rare_exome_snps_df["ExonicFunc.refGeneWithVer"].str.contains("nonsynonymous|stopgain|frameshift", na=False)
]

# Save results to designated filepath
functional_ultra_rare_snps.to_csv("", index=False)

print(f"Identified {len(functional_ultra_rare_snps)} functionally impactful ultra-rare SNPs.")

