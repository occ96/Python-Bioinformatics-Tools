
# Create list of amino acids given from prompt or read in data file
aa_list = ["Trp", "Arg", "Liu", "Ilu", "Asp"]

# Prompt the user for input of a.a. codon
# Could add check here to throw error if not 3 letters
codons = input("Please type a three letter codon: ")

# Set statement to false when an a.a. has been found
codon_found = False

# For loop to iterate through list of a.a. given with user input
for amino_acid in aa_list:
    # If codon from user is one of the a.a. in the list
    if codons == amino_acid:
        # then statement is True and a.a. identified
        codon_found = True
        break  # Break will exit the loop since a codon was found

# If codon has been found, print the message
# Else, print the a.a. hasnt been found or is not in the current list
if codon_found:
    print("Amino acid has been found in the list.")
else:
    print("Amino acid has not been found in the list. Try again.")
