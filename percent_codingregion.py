# Open the file containing DNA
with open("genomic_dna.txt", "r") as file:
    genomic_dna = file.read()

# Use variables to illustrate exon regions in DNA
start_exon = 0 # exon start
exon1_end = 63 # til the 63rd base pair
start_exon2 = 91 # runs from 91st base pair
exon2_end = len(genomic_dna)

# Extract exons and intron
exon = genomic_dna[start_exon:exon1_end]
exon_two = genomic_dna[start_exon2:exon2_end]
intron = genomic_dna[exon1_end:start_exon2]

# Write exons to "coding.txt"
with open("coding.txt", "w") as coding_file:
    coding_file.write(exon + exon_two)

# Write to noncoding file the intron region
with open("non_coding.txt", "w") as noncoding_file:
    noncoding_file.write(intron)

# Calculate percentage of coding sequence
ttl_length = len(genomic_dna)
code_length = len(exon) + len(exon_two)
percent = (code_length / ttl_length) * 100

# Print the coding percentage to two decimal places
print(f"Percent of coding region: {percent:.2f}%")
