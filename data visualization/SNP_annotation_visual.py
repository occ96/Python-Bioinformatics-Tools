import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
import re

# Function to prompt user for multiple file uploads
def upload_files():
    root = tk.Tk()
    root.withdraw()  # Hide main tkinter window
    file_paths = filedialog.askopenfilenames(title="Select Chromosome SNP Files", 
                                             filetypes=[("CSV Files", "*.csv")])
    return file_paths

# Step 1: Ask user to upload the files
file_paths = upload_files()
if not file_paths:
    print("No files selected. Exiting...")
    exit()

# Step 2: Load the uploaded CSV files
df_list = [pd.read_csv(file) for file in file_paths]
df = pd.concat(df_list, ignore_index=True).copy()  # Merge files and defragment

# Identify necessary columns
maf_col = "gnomad41_genome_AF"  # Use gnomAD genome-wide MAF
pval_col = "PVAL"  # Will extract from "Otherinfo11"
chr_col = next((col for col in df.columns if "chr" in col.lower()), None)
pos_col = next((col for col in df.columns if "start" in col.lower() or "position" in col.lower()), None)
otherinfo_col = "Otherinfo11"  # Column containing P-values
gene_col = "Gene.refGeneWithVer"  # Column containing gene annotations

# Extract P-values from "Otherinfo11"
def extract_pval(info_str):
    match = re.search(r'PVAL=([\d\.e-]+)', str(info_str))
    return float(match.group(1)) if match else None

df[pval_col] = df[otherinfo_col].apply(extract_pval)
df[pval_col] = pd.to_numeric(df[pval_col], errors='coerce')

# Ensure required columns exist
missing_cols = [c for c in [pval_col, maf_col, chr_col, pos_col, gene_col] if c not in df.columns]
if missing_cols:
    raise ValueError(f"Missing essential columns: {missing_cols}")

# Convert columns to numeric where necessary
df[maf_col] = pd.to_numeric(df[maf_col], errors='coerce')

# Compute -log10(P) for Manhattan plot
df = df.copy()  # Defragment before adding a new column
df["-log10(P)"] = -np.log10(df[pval_col])

# Identify SNPs passing the significance threshold
significance_threshold = 5
df_significant = df[df["-log10(P)"] >= significance_threshold]

# Display a table of significant SNPs with gene annotations
if not df_significant.empty:
    print("Significant SNPs (Above Threshold) with Gene Annotations:")
    print(df_significant[[chr_col, pos_col, pval_col, maf_col, "-log10(P)", gene_col]].sort_values(by="-log10(P)", ascending=False))
else:
    print("No SNPs passed the significance threshold.")

# ** Manhattan Plot for All Chromosomes**
plt.figure(figsize=(14, 6))
sns.scatterplot(data=df, x=pos_col, y="-log10(P)", hue=chr_col, palette="tab20", edgecolor=None, alpha=0.6, s=4)
plt.axhline(y=significance_threshold, color='red', linestyle='dashed', label="Genome-wide Significance")
plt.xlabel("Genomic Position")
plt.ylabel("-log10(P-value)")
plt.title("Manhattan Plot of SNPs on All Chromosomes")
plt.legend(markerscale=2, fontsize="small")
plt.show()

# ** MAF Distribution for All Chromosomes**
plt.figure(figsize=(12, 6))
sns.histplot(df[maf_col], bins=100, kde=True, color='blue', alpha=0.6, edgecolor='black')
plt.xlabel("Minor Allele Frequency (MAF)")
plt.ylabel("Count of SNPs")
plt.title("MAF Distribution for SNPs on All Chromosomes")
plt.xscale("log")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# ** Histogram for Ultra-Rare SNPs (MAF < 0.01) across All Chromosomes**
ultra_rare_filtered = df[df[maf_col] < 0.01]

plt.figure(figsize=(12, 6))
sns.histplot(ultra_rare_filtered[maf_col], bins=50, kde=True, color='red', alpha=0.6, edgecolor='black')
plt.xlabel("Minor Allele Frequency (MAF)")
plt.ylabel("Count of Ultra-Rare SNPs")
plt.title("Histogram of Ultra-Rare SNPs (MAF < 0.01) on All Chromosomes")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
