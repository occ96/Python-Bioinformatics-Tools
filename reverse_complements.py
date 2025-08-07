# Purpose: Check if 1st and 2nd DNA sequence strands are rev complements
# Returns to user if they are reverse complements or not

# Prompt the user to type 1st and 2nd DNA sequences
strand_one = input("Please type the 1st DNA sequence:  \n")
strand_two = input("Please type the 2nd DNA sequence: ")

# Per guidelines convert DNA to capital letters
DNA_upper = strand_one.upper()
DNA_upper_two = strand_two.upper()

# Double equal checks to verify if sequences same
# If else statement depends on input
if DNA_upper == DNA_upper_two:
    print("Sequences input by user are not reverse complements.")
else:
    print("Sequences input by user are reverse complements.")
