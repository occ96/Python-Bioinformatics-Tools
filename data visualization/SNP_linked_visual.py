# Purpose: To show linked chromosome data based on the breast cancer dataset. This will generate a histogram and a heatmap visualization.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog

# Function to let the user select multiple SNP .txt or .tsv files
def select_snp_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    snp_files = filedialog.askopenfilenames(
        title="Select SNP Files",
        filetypes=[("SNP Data Files", "*.txt;*.tsv"), ("Text Files", "*.txt"), ("TSV Files", "*.tsv")]
    )
    
    if not snp_files:
        print("No SNP files selected. Exiting.")
        return None
    
    return snp_files

# Function to load selected SNP files into a single DataFrame
def load_snp_data(snp_files):
    snp_data = []
    for file in snp_files:
        try:
            df = pd.read_csv(file, sep="\t", low_memory=False)
            snp_data.append(df)
        except Exception as e:
            print(f"Could not read {file}: {e}")
    
    if not snp_data:
        print("No valid SNP data loaded. Exiting.")
        return None

    df_all = pd.concat(snp_data, ignore_index=True)
    
    # Ensure numeric columns
    df_all["MAF"] = pd.to_numeric(df_all["MAF"], errors="coerce")
    df_all["R2"] = pd.to_numeric(df_all["R2"], errors="coerce")
    df_all["Dprime"] = pd.to_numeric(df_all["Dprime"], errors="coerce")

    # Extract chromosome numbers from "Coord" column
    df_all["Chromosome"] = df_all["Coord"].str.extract(r'chr(\d+)').astype(float)
    df_all["Position"] = df_all["Coord"].str.extract(r':(\d+)').astype(float)

    return df_all

# Function to generate Manhattan Plot
def plot_manhattan(df):
    plt.figure(figsize=(12, 6))
    plt.scatter(df["Position"], df["MAF"], c=df["Chromosome"], cmap="viridis", alpha=0.6)
    plt.xlabel("Genomic Position")
    plt.ylabel("Minor Allele Frequency (MAF)")
    plt.title("Manhattan Plot of SNPs")
    plt.colorbar(label="Chromosome")
    plt.show()

# Function to generate Minor Allele Frequency (MAF) Distribution Histogram
def plot_maf_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["MAF"], bins=50, kde=True, color="blue")
    plt.xlabel("Minor Allele Frequency (MAF)")
    plt.ylabel("Count of SNPs")
    plt.title("Distribution of Minor Allele Frequency")
    plt.show()

# Fixed Function to generate Linkage Disequilibrium (LD) Heatmap
def plot_ld_heatmap(df):
    # Ensure necessary columns exist
    if "RS_Number" not in df.columns or "R2" not in df.columns:
        print("Missing required columns for LD heatmap. Skipping visualization.")
        return
    
    # Group by RS_Number to ensure uniqueness, take the mean R² values
    df_ld = df.groupby("RS_Number", as_index=False)["R2"].mean()

    # Select a subset to prevent excessive heatmap size (first 50 SNPs)
    df_ld_subset = df_ld.head(50)

    # Convert the subset into a matrix for heatmap visualization
    ld_matrix = df_ld_subset.pivot(columns="RS_Number", values="R2")

    # Fill NaN values with 0 for visualization
    ld_matrix = ld_matrix.fillna(0)

    # Generate the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(ld_matrix, cmap="coolwarm", square=True, linewidths=0.5)
    plt.title("Linkage Disequilibrium (LD) Heatmap (R² Values)")
    plt.show()

# Main function to execute the workflow
def main():
    snp_files = select_snp_files()
    if not snp_files:
        return
    
    df_all = load_snp_data(snp_files)
    if df_all is None:
        return
    
    # Generate Visualizations
    plot_manhattan(df_all)
    plot_maf_distribution(df_all)
    plot_ld_heatmap(df_all)

# Run the program
if __name__ == "__main__":
    main()


